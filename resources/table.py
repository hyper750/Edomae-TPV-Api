from flask_jwt_extended import jwt_required
from flask_restful import Resource
from models import Table
from serialization import TableSchema


class TableResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self, id: int):
        table = Table.query.get(id)

        if not table:
            return '', 404
        
        return TableSchema().dump(table)

    def put(self, id: int):
        pass

    def delete(self, id: int):
        table = Table.query.get(id)

        if table:
            table.delete()
        
        return '', 204


class TablesResources(Resource):
    method_decorators = (jwt_required(),)

    def post(self):
        pass

    def get(self):
        pass
