from flask_cache import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
cache = Cache(config={'CACHE_TYPE':'redis'})


def ext_init(app):
    cache.init_app(app=app)
    db.init_app(app)
    Migrate(app=app, db=db)
    DebugToolbarExtension(app=app)


