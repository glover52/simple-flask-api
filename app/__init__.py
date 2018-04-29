from flask import Flask
from expiringdict import ExpiringDict
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from config import Config

app = Flask(__name__)
cache = ExpiringDict(max_len=100, max_age_seconds=30)
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

from app import routes