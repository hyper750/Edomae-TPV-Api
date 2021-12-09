from adapter.db import DB
from settings import LOCAL_IMATGES_DIR
from sqlalchemy import (
    BigInteger, Boolean, Column, String
)
from sqlalchemy.sql import expression
from utils.file_field import save_file_field
from werkzeug.datastructures import FileStorage

from .crud_model import CRUDModel


class Local(DB.Model, CRUDModel):
    __tablename__ = 'local'

    id = Column(BigInteger, primary_key=True)

    # Local enabled or not
    enabled = Column(Boolean, nullable=False, default=expression.true())

    # Local name, eg: Edomae or edomae claustre
    name = Column(String(length=124), nullable=False, unique=True)

    # Local imatge path
    imatge = Column(String(250), nullable=False)

    def save(self):
        if isinstance(self.imatge, FileStorage):
            # Save imatge to dir
            self.imatge = save_file_field(self.imatge, LOCAL_IMATGES_DIR)
        # Save instance
        return super().save()
