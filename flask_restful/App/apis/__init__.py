from flask_restful import Api

from App.apis.urls import SimpleResource, MovieResource, SecondMovieResource

api = Api()

def api_init(app):
    api.init_app(app)



api.add_resource(SimpleResource, '/simple_get/')
api.add_resource(MovieResource, '/movie/')
api.add_resource(SecondMovieResource, '/smovie/')



