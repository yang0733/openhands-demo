import threading
import time
from utils import process_data
from config import get_shared_resource, get_resource_lock

def worker(data, thread_id):
    for item in data:
        # Simulate some work
        # time.sleep(0.0001) # Removed sleep to increase race condition likelihood
        result = process_data(item, thread_id)
        print(f"Thread {thread_id}: Processed {item}, Result: {result}")

if __name__ == "__main__":
    data_items = list(range(1, 101)) # Increase data items to 100
    
    # Divide data for two threads
    data_thread1 = data_items[:len(data_items)//2]
    data_thread2 = data_items[len(data_items)//2:]

    thread1 = threading.Thread(target=worker, args=(data_thread1, 1))
    thread2 = threading.Thread(target=worker, args=(data_thread2, 2))

    print("Starting threads...")
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    shared_resource = get_shared_resource()
    print(f"All threads finished. Final counter value: {shared_resource['counter']}")
