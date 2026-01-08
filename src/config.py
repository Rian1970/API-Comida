from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

class ConfigMySQL:
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_DB = os.getenv("MYSQL_DB")

config_mysql = ConfigMySQL()
