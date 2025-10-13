from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import text


engine = create_engine(settings.database_url, pool_pre_ping=True)
session_local = sessionmaker(autocommit=False,autoflush=False,bind=engine)

base = declarative_base()
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

def init_db():
    from model.models import base #inportar despues de definir base
    base.metadata.create_all(bind=engine)
    print("--> DB correct")

# se ejecuta solo con python db.py
if __name__ == "__main__":
    print("1.Probando conexión con la base de datos...")
    try:
        with engine.connect() as connection:
            version = connection.execute(text("SELECT VERSION()")).scalar()
            print(f"--> Conexión exitosa a MariaDB ({version})")
    except Exception as e:
        print("--> Error al conectar con la base de datos:")
        print(e)