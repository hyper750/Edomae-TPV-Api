from flask_restful import Resource
from flask_jwt_extended import jwt_required


class TranslationResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self, id: int):
        pass
    
    def put(self, id: int):
        pass

    def delete(self, id: int):
        pass


class TranslationsResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self):
        pass

    def post(self):
        pass
