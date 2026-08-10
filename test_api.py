import os
import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient

TEST_DATABASE = Path(tempfile.gettempdir()) / "agendamento_test.db"
if TEST_DATABASE.exists():
    TEST_DATABASE.unlink()
os.environ["DATABASE_PATH"] = str(TEST_DATABASE)

from api import app  # noqa: E402


class AgendamentoApiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)
        cls.data = (date.today() + timedelta(days=1)).isoformat()
        cls.whatsapp_mock = patch("api.enviar_whatsapp")
        cls.enviar_whatsapp_mock = cls.whatsapp_mock.start()

    @classmethod
    def tearDownClass(cls):
        cls.whatsapp_mock.stop()
        cls.client.close()
        if TEST_DATABASE.exists():
            TEST_DATABASE.unlink()

    def test_lista_servicos_iniciais(self):
        response = self.client.get("/servicos")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json()), 4)

    def test_agendamento_conflitante_e_rejeitado(self):
        payload = {
            "nome_cliente": "Cliente de teste",
            "contato": "(48) 99999-0000",
            "servico_id": 1,
            "data": self.data,
            "horario": "08:00",
        }
        self.assertEqual(self.client.post("/agendamentos", json=payload).status_code, 201)
        self.assertEqual(self.enviar_whatsapp_mock.call_count, 2)
        conflict = self.client.post("/agendamentos", json=payload)
        self.assertEqual(conflict.status_code, 409)

    def test_horario_fora_do_intervalo_e_rejeitado(self):
        response = self.client.post(
            "/agendamentos",
            json={
                "nome_cliente": "Cliente de teste",
                "contato": "(48) 99999-0000",
                "servico_id": 1,
                "data": self.data,
                "horario": "08:15",
            },
        )
        self.assertEqual(response.status_code, 422)


if __name__ == "__main__":
    unittest.main()
