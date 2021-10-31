from adapter.db import DB, MA
from sqlalchemy import BigInteger, Column, Integer

# TODO: Add resource
class Table(DB.Model):
    __tablename__ = 'table'

    # Id of the table
    id = Column(BigInteger, primary_key=True)

    # Table number
    number = Column(Integer, nullable=False, unique=True)


class TableSchema(MA.Schema):
    class Meta:
        fields = (
            'id',
            'number',
        )
