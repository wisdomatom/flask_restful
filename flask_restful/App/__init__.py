from flask import Flask

from App.apis import api_init
from App.app_1000.views import movie_blue
from App.ext import ext_init
from App.modles import Person, Movies, PersonMovie
from App.setting import Config



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.debug = True
    ext_init(app)
    api_init(app)


    app.register_blueprint(blueprint=movie_blue)

    return app



