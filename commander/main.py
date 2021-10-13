from flask import Flask

from commander.settings import FLASK_CONFIG

app = Flask('Commander')

# Configure app
app.config.update(FLASK_CONFIG)

if __name__ == '__main__':
    app.run()
