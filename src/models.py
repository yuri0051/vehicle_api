"""Vehicle API Models"""
from sqlalchemy import Column, Integer, String, UniqueConstraint
from src.database import Base

class Car(Base):
    """Car Model"""
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    make = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    rate = Column(Integer)
    UniqueConstraint(make, model)

    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.rate = kwargs.get('rate')