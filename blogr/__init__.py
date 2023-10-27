import locale

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_object('config.Config')
    db.init_app(app)

    from flask_ckeditor import CKEditor
    ckeditor = CKEditor(app)

    try:
        locale.setlocale(locale.LC_ALL,'es_ES')
    except locale.Error:
        pass

    from blogr import home
    app.register_blueprint(home.bp)

    from blogr import auth
    app.register_blueprint(auth.bp)

    from blogr import post
    app.register_blueprint(post.bp)

    from .models import User, Post

    with app.app_context():
        db.create_all()

    return app









