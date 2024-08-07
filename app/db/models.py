from sqlalchemy import Column, Integer, Float, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Deposit(Base):
    __tablename__ = "deposits"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    amount = Column(Float)
