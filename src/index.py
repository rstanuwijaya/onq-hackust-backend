print('starting flask backend server')
from router.api import api
from flask import *

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')


