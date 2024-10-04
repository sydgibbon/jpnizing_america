from flask import Flask
from config import Config
from flask_jwt_extended import JWTManager
from db import db_session, init_db
from seed import seed_database

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)  # Carga la configuración

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
    
init_db()

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "DEFINITELY_NOT_SAFE_SECRET"
jwt = JWTManager(app)

from core import auth
app.register_blueprint(auth.auth_bp)


try:
    seed_database()
finally:
    if __name__ == "__main__":
        app.run(host="0.0.0.0", debug=True)

