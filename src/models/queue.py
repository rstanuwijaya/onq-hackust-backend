#%%
import time
import uuid

class Queue:
    users = None
    clients = None
    queues = None
    queues_processed= None

    def add_user(self, data):
        entry = dict()
        user_id = uuid.uuid4()
        entry['data'] = data
        entry['queue'] = list()
        entry['queue_processed'] = list()
        self.users[str(user_id)] = entry
        print('new user user_id %s \n %s' % (user_id, data))
        return str(user_id)

    def add_client(self, data):
        entry = dict()
        client_id = uuid.uuid4()
        entry['data'] = data
        entry['last_queue_number'] = 0
        entry['queue'] = list()
        entry['queue_processed'] = list()
        self.clients[str(client_id)] = entry
        print('new user client_id %s \n %s' % (client_id, data))
        return str(client_id)
        
    def add_queue(self, user_id, client_id, data):
        if user_id not in self.users or client_id not in self.clients:
            raise Exception('id does not match database')
        queue_id = uuid.uuid4()
        entry = dict() 
        entry['id'] = str(queue_id)
        queue_number = last_queue_number + 1
        entry['alias'] = str(queue_number)
        entry['user_id'] = user_id
        entry['client_id'] = client_id
        entry['data'] = data
        entry['time'] = time.asctime()
        self.clients[client_id]['last_queue_number'] = queue_number
        entry['status'] = 'active'
        self.queues.append(entry)
        self.queues_processed.append(entry)
        self.users[user_id]['queue'].append(str(queue_id))
        self.clients[client_id]['queue'].append(str(queue_id))
        self.users[user_id]['queue_processed'].append(str(queue_id))
        self.clients[client_id]['queue_processed'].append(str(queue_id))
        print('new user queue_id %s \n %s' % (queue_id, data))
        return str(queue_id)

    def reset_queue_number(self, client_id):
        self.clients['last_queue_number'] = 0

    def check_current_queue(self, queue_id, client_id):
        client = clients['client_id']
        processed_queue = client['processed_queue']
        active_queue = [q['id'] for q in processed_queue if q['status'] == 'active']
        active_queue.index(queue_id)

    def revive_queue(self, queue_id, client_id, new_order):
        try:
            client = clients['client_id']
        except:
            raise Exception('client_id does not match database')
        queue = [q for q in client['queue'] if q['id'] == 'queue_id']
        if queue is []:
            raise Exception('queue_id not found')
        else:
            queue = queue[0]
        if queue['status'] == 'active':
            raise Exception('queue is still active')
        if queue['status'] == 'dead':
            raise Exception('queue is already dead')
        queue['status'] = 'active'
        active_queue = [q['id'] for q in client['processed_queue'] if q['status'] == 'active']
        queue_to_be_shifted = active_queue[new_order]
        new_index = processed_queue.index(queue_to_be_shifted)
        processed_queue.remove(queue)

    def pop_queue(self, queue_id):
        queue = [x for x in self.queues_processed if x['id']==queue_id]
        if queue == []: return('tai')
        queue = queue[0]
        queue['status'] = 'grace'
        return queue_id

    def terminate_queue(self, queue_id):
        queue = [x for x in self.queues_processed if x['id']==queue_id]
        if queue == []: raise('tai')
        queue = queue[0]
        queue['status'] = 'dead'
        user_id = queue['user_id']
        client_id = queue['client_id']
        self.users[user_id]['queue_processed'].remove(queue_id) 
        self.clients[client_id]['queue_processed'].remove(queue_id)
        self.queues_processed.remove(queue)
        return queue_id

    def __init__(self):
        self.users = dict()
        self.clients = dict()
        self.queues = list()
        self.queues_processed = list()

# a = Queue()
# stefan = {'name':'stefan'}
# ferris = {'name':'ferris'}

# saizer = {'name':'saizer'}

# id_stefan = a.add_user(stefan)
# id_ferris = a.add_user(ferris)
# id_saizer = a.add_client(saizer)

# id_queue1 = a.add_queue(id_stefan, id_saizer, 'tae')
# a.pop_queue(id_queue1)

# print(a.queues_processed)

# a.terminate_queue(id_queue1)

# print(a.queues_processed)
# %%
