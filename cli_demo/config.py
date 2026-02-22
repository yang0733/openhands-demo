
import threading

_shared_resource = {
    'counter': 0
}

_resource_lock = threading.Lock()

def get_shared_resource():
    return _shared_resource

def get_resource_lock():
    return _resource_lock
