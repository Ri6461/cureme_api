from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
from os import environ as env
from os import getcwd as pwd
from os import path

load_dotenv()
host, user, passwd, db_name = env.get("DB_HOST"), env.get("DB_USER"), env.get("DB_PASS"), env.get("DB_NAME") 
db_service_name = "postgresql"
SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{passwd}@{host}/{db_name}"
if env.get("USE_SQLITE").lower() == "yes":
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{pwd()}/{db_name}.db"
    db_service_name = "sqlite"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL #, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def init_db():
    if db_service_name == 'postgresql':
        # Connect to the default database to check if the target database exists
        conn = psycopg2.connect(dbname="postgres", user=user, password=passwd, host=host)
        conn.autocommit = True
        cursor = conn.cursor()

        # Check if the database exists
        cursor.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), [db_name])
        exists = cursor.fetchone()

        if not exists:
            # Create the database
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
            print(f"Database {db_name} created!")

        cursor.close()
        conn.close()

        # Create tables if they don't exist
        Base.metadata.create_all(bind=engine)
    else:
        if not path.isfile(SQLALCHEMY_DATABASE_URL.split('://')[1]):
            Base.metadata.create_all(bind=engine)
    print("\n[+] Tables initialized!", end='\n'*2)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Call the init_db function
if __name__ == "__main__":
    init_db()
