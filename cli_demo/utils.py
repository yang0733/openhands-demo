from config import get_shared_resource

def process_data(item, thread_id):
    shared_resource = get_shared_resource()
    # This is a classic non-thread-safe read-modify-write operation
    # It is prone to race conditions.
    current_value = shared_resource["counter"]
    # Simulate some non-atomic operation that takes time
    # In a real scenario, this might be complex calculations or I/O
    # Introduce a small delay to increase the chance of context switching
    for _ in range(100000): pass 
    new_value = current_value + item
    shared_resource["counter"] = new_value
    return shared_resource["counter"]
