from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql import expression
from sqlalchemy.types import DateTime


class UTCNow(expression.FunctionElement):
    type = DateTime()


@compiles(UTCNow, 'postgresql')
def pg_utcnow(element, compiler, **kwargs) -> str:
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"


@compiles(UTCNow, 'mssql')
def mysql_utcnow(element, compiler, **kw):
    return "GETUTCDATE()"
