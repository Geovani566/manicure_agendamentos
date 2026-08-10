"""Inicializa o banco SQLite usando o mesmo esquema da aplicação."""

from api import criar_tabelas


if __name__ == "__main__":
    criar_tabelas()
    print("Banco inicializado com sucesso.")
