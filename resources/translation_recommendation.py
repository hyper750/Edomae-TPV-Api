from parser import parse_translation_recommendation_query

from flask_jwt_extended import jwt_required
from flask_restful import Resource
from logic.translation_recommendation import (
    get_translation_recommendations_keys
)
from models import Language, Translation


class TranslationRecomendationResource(Resource):
    method_decorators = (jwt_required(),)

    def get(self):
        keys: set = get_translation_recommendations_keys(
            **parse_translation_recommendation_query()
        )

        recommendations = []

        # Add the keys that doesn't exists as translations
        for key in keys:
            for language in Language:
                if not Translation.query.filter_by(key=key, language=language).exists():
                    recommendations.append(dict(
                        key=key,
                        language=language.value
                    ))
        
        return recommendations
