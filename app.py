from flask import Flask
from flask_migrate import Migrate

from adapter.db import DB, MA
from logic.user import JWT
from routes import API_ROUTES, TICKET_API
from settings import FLASK_CONFIG, CORS_SETTINGS
from flask_cors import CORS

app = Flask('Commander')

# Configure app
app.config.update(FLASK_CONFIG)

# Configure cross origin
CORS(app, resources=CORS_SETTINGS)

# Initialize database
DB.init_app(app)

# Initialize database migrations
migrate = Migrate(app, DB)

# Initialize database serializer
MA.init_app(app)

# Initialize jwt
JWT.init_app(app)

# Initialize api routes
API_ROUTES.init_app(app)

# Initialize ticket routes
TICKET_API.init_app(app)

if __name__ == '__main__':
    app.run()
