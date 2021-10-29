from adapter.db import DB, MA
from sqlalchemy import BigInteger, Column, Integer


class Table(DB.Model):
    __tablename__ = 'table'

    # Id of the table
    id = Column(BigInteger, primary_key=True)

    # Table number
    table_number = Column(Integer, nullable=False, unique=True)


class TableSchema(MA.Schema):
    class Meta:
        fields = (
            'id',
            'table_number',
        )
