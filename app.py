from flask import Flask

from settings import FLASK_CONFIG, DB, MA

app = Flask('Commander')

# Configure app
app.config.update(FLASK_CONFIG)

# Initialize database
DB.init_app(app)

# Initialize db serializer
MA.init_app(app)

# TODO: Initialize jwt

# TODO: Initialize api resources

if __name__ == '__main__':
    app.run()
