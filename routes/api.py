from flask_restful import Api
from resources import (
    Auth, MealCategoriesResource, MealCategoryResource,
    MealResource, MealsResource,
    PaymentMethodsResource, PaymentMethodResource,
    CommandResource, CommandsResource,
    TableResource, TablesResources,
    CommandMealResource, CommandMealsResource
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

# Payment methods
API_ROUTES.add_resource(PaymentMethodResource, '/paymentMethod/<int:id>')
API_ROUTES.add_resource(PaymentMethodsResource, '/paymentMethod')

# Commands
API_ROUTES.add_resource(CommandResource, '/command/<int:id>')
API_ROUTES.add_resource(CommandsResource, '/command')

# Meal per command
API_ROUTES.add_resource(CommandMealResource, '/commandMeal/<int:id>')
API_ROUTES.add_resource(CommandMealsResource, '/commandMeal')

# Table
API_ROUTES.add_resource(TableResource, '/table/<int:id>')
API_ROUTES.add_resource(TablesResources, '/table')
