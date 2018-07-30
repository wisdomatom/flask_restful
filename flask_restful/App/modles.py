import datetime

from App.ext import db




class Movies(db.Model):
    m_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    m_name = db.Column(db.String(64), nullable=False, unique=True)
    leading_actor = db.Column(db.String(64), nullable=False)
    show_time = db.Column(db.DateTime, default=datetime.datetime.now())

    personmovie = db.relationship('PersonMovie', backref='movie')
    def to_dict(self):
        return {'m_name':self.m_name, 'leading_actor':self.leading_actor, 'show_time':self.show_time}

class Person(db.Model):
    p_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    p_name = db.Column(db.String(32), nullable=False)
    # movie = db.Column(db.String(64), db.ForeignKey(Movies.m_name))
    personmovie = db.relationship('PersonMovie', backref='person')

class PersonMovie(db.Model):
    pm_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    p_id = db.Column(db.Integer, db.ForeignKey(Person.p_id))
    m_id = db.Column(db.Integer, db.ForeignKey(Movies.m_id))



