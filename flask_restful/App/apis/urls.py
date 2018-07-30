from flask import request
from flask_restful import fields, Resource, marshal_with, marshal, reqparse

from App.ext import db, cache
from App.modles import Movies


simple_fields = {
    'hello': fields.String,
    'status':fields.Integer,
}

class SimpleResource(Resource):
    @marshal_with(simple_fields)
    def get(self):
        return {'hello':'flask_restful', 'status':201}

movie_fields = {
    'm_name':fields.String,
    'leading_actor':fields.String,
    # 'show_time': fields.datetime,
}
movie_resource_fields = {
    'msg': fields.String,
    'data': fields.Nested(movie_fields)
}
class MovieResource(Resource):
    def get(self):
        m_id = int(request.args.get('m_id'))
        movie = Movies.query.get(m_id)
        return marshal({'msg':'查询成功', 'data': movie.to_dict(), 'status': 202}, movie_resource_fields)

    def post(self):
        m_name = request.form.get('m_name')
        leading_actor = request.form.get('leading_actor')

        movie = Movies()
        movie.m_name = m_name
        movie.leading_actor = leading_actor
        db.session.add(movie)
        db.session.commit()
        return {'msg': '添加成功', 'status':200}


second_movie_fields = {
    'm_id' : fields.Integer,
    'm_name': fields.String,
    'leading_actor': fields.String,
}

sc_resource_movie_fields = {
    'msg': fields.String,
    'data': fields.Nested(second_movie_fields),

}

parse = reqparse.RequestParser()
parse.add_argument('m_id', type=int, help='没有查询到此电影id', required=True)

post_movie_parse = parse.copy()
post_movie_parse.add_argument('m_name', type=str, help='电影名称不合法', required=True)
post_movie_parse.add_argument('leading_actor', type=str, help='没有输入主演名', required= True)

def key_get():
    return str(request.url) + request.remote_addr

class SecondMovieResource(Resource):
    @cache.cached(timeout=60, key_prefix=key_get)
    @marshal_with(sc_resource_movie_fields)
    def get(self):

        my_parse = parse.parse_args()
        m_id = my_parse.get('m_id')
        movie = Movies.query.get(m_id)

        return {'msg':'200', 'data': movie}

    @marshal_with(sc_resource_movie_fields)
    def post(self):
        my_parse = post_movie_parse.parse_args()
        m_id = my_parse.get('m_id')
        m_name = my_parse.get('m_name')
        leading_actor = my_parse.get('leading_actor')
        movie = Movies.query.get(m_id)
        movie.m_name = m_name
        movie.leading_actor = leading_actor
        db.session.add(movie)
        db.session.commit()
        return {'msg':'修改成功','data':movie}









