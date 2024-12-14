import datetime
import os

import sqlalchemy
from dotenv import load_dotenv
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import sessionmaker

load_dotenv()

DB_URL = os.getenv("DB_URL")

engine = sqlalchemy.create_engine(DB_URL)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = sqlalchemy.orm.declarative_base()


class Url(Base):
    __tablename__ = "urls"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    short_url = Column(String)
    full_url = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now())
