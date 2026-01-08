from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

class ConfigMySQL:
    ENV = os.getenv("ENV", "dev")

    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_DB = os.getenv("MYSQL_DB")

    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")

    INSTANCE_CONNECTION_NAME = os.getenv("INSTANCE_CONNECTION_NAME")

    @classmethod
    def database_url(cls) -> str:
        if cls.ENV == "prod":
            return (
                f"mysql+pymysql://{cls.MYSQL_USER}:{cls.MYSQL_PASSWORD}@/"
                f"{cls.MYSQL_DB}"
                f"?unix_socket=/cloudsql/{cls.INSTANCE_CONNECTION_NAME}"
            )

        # dev / local
        return (
            f"mysql+pymysql://{cls.MYSQL_USER}:{cls.MYSQL_PASSWORD}"
            f"@{cls.MYSQL_HOST}:{cls.MYSQL_PORT}/{cls.MYSQL_DB}"
        )
