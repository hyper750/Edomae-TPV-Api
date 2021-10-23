from adapter.db import DB


class CRUDModel:
    def get_pk(self):
        return 'id'

    def save(self):
        if getattr(self, self.get_pk()) is None:
            DB.session.add(self)
        return DB.session.commit()

    def delete(self):
        DB.session.delete(self)
        return DB.session.commit()
