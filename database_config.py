from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("SQLITE_URL_DB")

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine, autocommit=False)
session = Session()

Base = declarative_base()

