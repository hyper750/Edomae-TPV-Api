from flask_restful import Api
from resources import (
    Auth, MealCategoriesResource, MealCategoryResource,
    MealResource, MealsResource
)

API_ROUTES = Api()

# Auth route
API_ROUTES.add_resource(Auth, '/auth')

# Meal routes
API_ROUTES.add_resource(MealResource, '/meal/<int:id>')
API_ROUTES.add_resource(MealsResource, '/meal')

# Meal category rotues
API_ROUTES.add_resource(MealCategoryResource, '/mealCategory/<int:id>')
API_ROUTES.add_resource(MealCategoriesResource, '/mealCategory')
