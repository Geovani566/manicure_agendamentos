# Florescer Studio — Agendamento

Aplicação de agendamento para serviços de manicure, construída com FastAPI, SQLite e uma página HTML estática.

## Como executar

1. Crie e ative um ambiente virtual Python 3.11+.
2. Instale as dependências: `pip install -r requirements.txt`.
3. Copie `.env.example` para `.env` e informe os dados da Evolution API (ou configure as variáveis no ambiente do sistema).
4. Execute: `python main.py`.
5. Acesse `http://127.0.0.1:8000`.

Para desenvolvimento com recarga automática, defina `RELOAD=true`. Não use essa opção em produção.

## Configuração

- `EVOLUTION_API_KEY`: chave privada da Evolution API. Se ausente, o agendamento é salvo e o WhatsApp é ignorado.
- `EVOLUTION_URL` e `EVOLUTION_INSTANCE_NAME`: dados da instância da Evolution API.
- `MANICURE_NUMERO`: telefone que receberá o aviso de cada novo agendamento, com DDI e DDD.
- `ALLOWED_ORIGINS`: domínios autorizados para CORS, separados por vírgula.
- `DATABASE_PATH`: caminho opcional do banco SQLite; útil em testes e deploy.

As variáveis do ambiente do sistema têm prioridade sobre o arquivo `.env`. No PowerShell, por exemplo: `$env:EVOLUTION_API_KEY = "sua-chave"`. Nunca versione `.env`, banco de produção ou chaves de API.

## Testes

Execute `python -m unittest -v`. Os testes usam um banco temporário separado e verificam a listagem de serviços, a reserva e o bloqueio de conflito.
