from adapter.db import DB
from sqlalchemy import BigInteger, Column, Integer

# TODO: Add resource
class Table(DB.Model):
    __tablename__ = 'table'

    # Id of the table
    id = Column(BigInteger, primary_key=True)

    # Table number
    number = Column(Integer, nullable=False, unique=True)
