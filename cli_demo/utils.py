from config import get_shared_resource, get_resource_lock

def process_data(item, thread_id):
    shared_resource = get_shared_resource()
    resource_lock = get_resource_lock()
    with resource_lock:
        shared_resource["counter"] += item
    return shared_resource["counter"]
