import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()


class Config:
    # =========================================================
    # CHAVE SECRETA DO FLASK
    # =========================================================
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")

    # =========================================================
    # CONEXÃO COM O POSTGRESQL DA AZURE
    # =========================================================
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://adminagrolink@agrolink:%2BRavy123@agrolink.postgres.database.azure.com:5432/postgres?sslmode=require"
    )

    # =========================================================
    # DESATIVA MODIFICAÇÕES DO SQLALCHEMY
    # =========================================================
    SQLALCHEMY_TRACK_MODIFICATIONS = False
