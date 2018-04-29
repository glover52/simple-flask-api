from flask import Flask
from expiringdict import ExpiringDict
from pylibmc import Client
import os
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from config import Config

app = Flask(__name__)
cache = ExpiringDict(max_len=100, max_age_seconds=30)
servers = os.environ.get('MEMCACHIER_SERVERS', '').split(',')
user = os.environ.get('MEMCACHIER_USERNAME', '')
passw = os.environ.get('MEMCACHIER_PASSWORD', '')

mc = Client(servers, binary=True,
                    username=user, password=passw,
                    behaviors={
                      # Faster IO
                      "tcp_nodelay": True,

                      # Keep connection alive
                      'tcp_keepalive': True,

                      # Timeout for set/get requests
                      'connect_timeout': 2000, # ms
                      'send_timeout': 750 * 1000, # us
                      'receive_timeout': 750 * 1000, # us
                      '_poll_timeout': 2000, # ms

                      # Better failover
                      'ketama': True,
                      'remove_failed': 1,
                      'retry_timeout': 2,
                      'dead_timeout': 30,
                    })
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

from app import routes