from parser import parse_object_table, parse_query_table

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
        table = Table.query.get(id)

        if not table:
            return '', 404

        for key, value in parse_query_table().items():
            setattr(table, key, value)

        table.save()

        return TableSchema().dump(table)

    def delete(self, id: int):
        table = Table.query.get(id)

        if table:
            table.delete()

        return '', 204


class TablesResources(Resource):
    method_decorators = (jwt_required(),)

    def post(self):
        table = Table(
            **parse_object_table()
        )

        table.save()

        return TableSchema().dump(table)

    def get(self):
        tables = Table.query.filter_by(
            **parse_query_table()
        )

        return TableSchema(many=True).dump(tables)
