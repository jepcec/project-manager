#================================================================
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
load_dotenv()


class Settings:
    DATABASE_USER: str = os.getenv("DATABASE_USER")
    DATABASE_PASSWORD: str =os.getenv("DATABASE_PASSWORD")
    DATABASE_HOST: str =os.getenv("DATABASE_HOST")
    DATABASE_PORT: int =int(os.getenv("DATABASE_PORT"))
    DATABASE_NAME: str =os.getenv("DATABASE_NAME")

    DATABASE_URL = (
        f"mariadb+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@"
        f"{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    )

settings = Settings()
engine = create_engine(settings.DATABASE_URL,echo=True)
session = sessionmaker(autocommit=False,autoflush=False,bind=engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def test_connection():
    from sqlalchemy import text
    from sqlalchemy.exc import SQLAlchemyError
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("resultado exitoso: ", result.scalar())
            return "conexion exitosa a db"
    except SQLAlchemyError as e:
        print("Error de conexion: ", str(e))
        return "error conexion a db"
