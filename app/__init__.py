from flask import Flask
from pylibmc import Client
import os

app = Flask(__name__)
servers = os.environ.get('MEMCACHIER_SERVERS', '').split(',')
user = os.environ.get('MEMCACHIER_USERNAME', '')
passw = os.environ.get('MEMCACHIER_PASSWORD', '')
# Client config obtained from https://devcenter.heroku.com/articles/memcachier#python
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

from app import routes