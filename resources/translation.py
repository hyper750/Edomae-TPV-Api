from parser import parse_translation_object, parse_translation_query

from flask_jwt_extended import jwt_required
from flask_restful import Resource
from models import Translation
from serialization import TranslationSchema


class TranslationResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self, id: int):
        translation = Translation.query.get(id)

        if not translation:
            return '', 404

        return TranslationSchema().dump(translation)

    def put(self, id: int):
        translation = Translation.query.get(id)

        if not translation:
            return '', 404

        for key, value in parse_translation_query().items():
            setattr(translation, key, value)

        translation.save()

        return TranslationSchema().dump(translation)

    def delete(self, id: int):
        translation = Translation.query.get(id)
        if translation:
            translation.delete()
        return '', 204


class TranslationsResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self):
        translations = Translation.query.filter_by(
            **parse_translation_query()
        ).order_by(Translation.key, Translation.language)
        return TranslationSchema(many=True).dump(translations)

    def post(self):
        translation = Translation(
            **parse_translation_object()
        )
        translation.save()
        return TranslationSchema().dump(translation), 201

# TODO: Optionally add language parameter
# If is not passed by parameter, use the original key (name, description whatever)
# If is passed by parameter the language
# params = parse_meal_query()
# if lang := params.get('lang')
#     meal.name = translation(meal.name, lang)
#     meal.description = translation(meal.description, lang)
