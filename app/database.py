from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2, hashlib
from psycopg2 import sql
from dotenv import load_dotenv
from os import environ as env
from os import getcwd as pwd
from os import path

load_dotenv()
host, user, passwd, db_name = env.get("DB_HOST"), env.get("DB_USER"), env.get("DB_PASS"), env.get("DB_NAME") 
db_service_name, secret = "postgresql", env.get("GOOGLE_CLIENT_SECRET")
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
            print(f"\n[+]Database {db_name} created!", end='\n'*2)

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

def skip_cipher(string_a, string_b):
    # Determine the length of the longer string
    max_len = max(len(string_a), len(string_b))
    
    # Initialize the result as an empty list
    result = []
    
    # Loop through the maximum length
    for i in range(max_len):
        if i < len(string_a):
            result.append(string_a[i])
        if i < len(string_b):
            result.append(string_b[i])
    
    # Join the list into a string and return it
    return ''.join(result)


def digest(string):
    h1 = hashlib.sha512(string.encode()).hexdigest()
    h2 = hashlib.sha512(h1.encode()).hexdigest()
    h1, h2 = h2[:64], h2[64:]
    h1 = skip_cipher(h1, h2)
    h2 = hashlib.sha512(h1.encode()).hexdigest()
    return skip_cipher(h1, h2)


# Call the init_db function
if __name__ == "__main__":
    init_db()
