from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()

def create_app(config=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)

    db.init_app(app)

    from app.posts.routes import bp as posts_bp
    app.register_blueprint(posts_bp)


    @app.route('/')
    def hello():
        return render_template('index.html')

    return app