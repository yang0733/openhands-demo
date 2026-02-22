# OpenHands CLI Demo: The Autonomous Bug Hunter

## Introduction (Narrator)

"Welcome to the OpenHands CLI demo. Today, we'll tackle a common, yet insidious problem in concurrent programming: the **race condition**. Traditional AI-assisted IDEs like Cursor or Claude Code might help you identify potential issues or suggest fixes for individual lines of code. But what happens when the bug spans multiple files, requires understanding thread interactions, and needs autonomous verification? This is where OpenHands shines."

"Our scenario involves a simple Python application that uses multiple threads to process a list of numbers and update a shared counter. Due to a lack of proper synchronization, the final count is often incorrect and inconsistent, a classic symptom of a race condition."

## Step 1: Demonstrating the Race Condition (Live Demo - Run `test_race_condition.py`)

"Let's first observe the bug in action. We have a test script, `test_race_condition.py`, that runs our `main.py` application multiple times and reports the final counter value. The expected sum of numbers from 1 to 100 is 5050. Watch closely as we execute the test."

```bash
python3 cli_demo/test_race_condition.py
```

*(Expected Output: Inconsistent final counter values, or consistently incorrect values, and a 'Race condition detected' message.)*

"As you can see, the final counter values are inconsistent across runs, or consistently incorrect. This non-deterministic behavior is the hallmark of a race condition, making it incredibly difficult to debug manually."

## Step 2: OpenHands to the Rescue (Narrator)

"Now, let's unleash OpenHands. Instead of us meticulously debugging each file, we'll give OpenHands a high-level goal: 'Fix the race condition in the multi-threaded counter application and ensure the final sum is consistently 5050.'"

"OpenHands, operating in its CLI mode, will autonomously analyze the codebase, identify the shared resource and the lack of synchronization, implement the necessary threading locks, and then verify its fix using the provided test script. All of this, with minimal human intervention."

*(Simulate OpenHands execution - this would be a pre-recorded video or a highly controlled live run)*

## Step 3: Verifying the Fix (Live Demo - Run `test_race_condition.py` again)

"OpenHands has completed its task. Let's re-run our `test_race_condition.py` to see if the bug has been squashed."

```bash
python3 cli_demo/test_race_condition.py
```

*(Expected Output: Consistent final counter values of 5050 across all runs, and a 'No race condition detected' message.)*

"Success! Every run now yields the correct and consistent sum of 5050. OpenHands didn't just suggest a fix; it understood the problem, implemented the solution, and verified its correctness, all autonomously."

## Conclusion (Narrator)

"This CLI demo showcases OpenHands' ability to act as an autonomous agent, tackling complex, multi-file engineering problems with a high degree of reliability. It goes beyond mere code assistance, providing a powerful platform for automated software development and bug fixing, freeing developers to focus on higher-level design and innovation."

## OpenHands Fix (For Demo Purposes - Agent would generate this)

*(This section would be the actual code changes OpenHands would make. I will add this after the agent has 'fixed' the code.)*

**config.py (after fix)**
```python
import threading

_shared_resource = {
    'counter': 0
}

_resource_lock = threading.Lock()

def get_shared_resource():
    return _shared_resource

def get_resource_lock():
    return _resource_lock
```

**utils.py (after fix)**
```python
from config import get_shared_resource, get_resource_lock

def process_data(item, thread_id):
    shared_resource = get_shared_resource()
    resource_lock = get_resource_lock()
    with resource_lock:
        shared_resource["counter"] += item
    return shared_resource["counter"]
```

**main.py (after fix - no changes needed for the fix itself, but for clarity)**
```python
import threading
import time
from utils import process_data
from config import get_shared_resource

def worker(data, thread_id):
    for item in data:
        time.sleep(0.0001) # Small sleep to simulate work, but not critical for race condition with lock
        result = process_data(item, thread_id)
        print(f"Thread {thread_id}: Processed {item}, Result: {result}")

if __name__ == "__main__":
    data_items = list(range(1, 101)) # Increased data items to 100
    
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
```
