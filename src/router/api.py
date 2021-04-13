#%%
import sys
sys.path.append('..')

import sqlite3
from flask import *
from models.queue import Queue
from querystring_parser import parser
api = Blueprint('api', __name__)
queue = Queue()

@api.route('/')
def index():
    return 'at root'

@api.route('/add_user/', methods=['POST'])
def add_user():
    request_data = request.get_json()
    try:
        data = request_data['data']
        user_id = queue.add_user(data)
    except:
        print('cannot parse query')
        return 'Bad Request', 400
    return str(user_id)


@api.route('/add_client/', methods=['POST'])
def add_client():
    request_data = request.get_json()
    try:
        data = request_data['data']
        client_id = queue.add_client(data)
    except:
        print('cannot parse query')
        return 'Bad Request', 400
    return str(client_id)

@api.route('/add_queue/', methods=['POST'])
def add_queue():
    request_data = request.get_json()
    try:
        user_id = request_data['user_id']
        client_id = request_data['client_id']
        data = request_data['data']
        queue_id = queue.add_queue(user_id, client_id, data)
    except Exception as exc:
        print(exc)
        print('Cannot add queue')
        return 'Bad Request', 400
    return str(queue_id)

@api.route('/pop_queue/', methods=['POST'])
def pop_queue():
    request_data = request.get_json()
    try:
        queue_id = request_data['queue_id']
        queue_id = queue.pop_queue(data)
    except:
        print('cannot parse query')
        return 'Bad Request', 400
    print('popped queue %s \n %s' % (queue_id, data))
    return str(queue_id)

@api.route('/termintated_queue/', methods=['POST'])
def terminate_queue():
    request_data = request.get_json()
    try:
        queue_id = request_data['queue_id']
        queue_id = queue.terminate_queue(data)
    except:
        print('cannot parse query')
        return 'Bad Request', 400
    print('terminated queue %s \n %s' % (queue_id, data))
    return str(queue_id)

@api.route('/check_user_queue/', methods=['GET'])
def check_user_queue():
    user_id = request.args.get('user_id')
    user = queue.clients[user_id]
    print(f'checking user_id {user_id}')
    return str(users['queue_processed'])

@api.route('/check_client_queue/', methods=['GET'])
def check_client_queue():
    client_id = request.args.get('client_id')
    client = queue.clients[client_id]
    print(f'checking client_id {client_id}')
    return str(client['queue_processed'])

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)

# %%
