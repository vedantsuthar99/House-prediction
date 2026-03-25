from sqlalchemy import Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class House(Base):
    __tablename__ = "houses"
    id = Column(Integer, primary_key=True, index=True)
    area = Column(Float)
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    price = Column(Float)