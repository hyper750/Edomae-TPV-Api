from parser import parse_object_payment_method, parse_query_payment_method

from flask_jwt_extended import jwt_required
from flask_restful import Resource
from models import PaymentMethod
from serialization import PaymentMethodSchema


class PaymentMethodResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self, id: int):
        payment_method = PaymentMethod.query.get(id)

        if not payment_method:
            return '', 404

        return PaymentMethodSchema().dump(payment_method)

    def put(self, id: int):
        payment_method = PaymentMethod.query.get(id)

        if not payment_method:
            return '', 404

        for key, value in parse_query_payment_method().items():
            setattr(payment_method, key, value)

        payment_method.save()

        return PaymentMethodSchema().dump(payment_method)

    def delete(self, id: int):
        payment_method = PaymentMethod.query.get(id)
        if payment_method:
            payment_method.delete()
        return '', 204


class PaymentMethodsResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self):
        payment_methods = PaymentMethod.query.filter_by(
            **parse_query_payment_method()
        )
        return PaymentMethodSchema(many=True).dump(payment_methods)

    def post(self):
        payment_method = PaymentMethod(
            **parse_object_payment_method()
        )
        payment_method.save()
        return PaymentMethodSchema().dump(payment_method)
