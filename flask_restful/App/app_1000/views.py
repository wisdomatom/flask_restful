from flask import Blueprint, request

from App.modles import Movies

movie_blue = Blueprint('movie_blue', __name__)

@movie_blue.route('/check/')
def check():
    m_id = request.args.get('m_id')
    movie = Movies.query.get(m_id)
    return '查询成功'