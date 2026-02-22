import subprocess
import os
import re

def run_main_and_get_final_counter():
    # Reset config.py's counter for each run
    # Assuming config.py is in the same directory as main.py
    config_path = os.path.join(os.path.dirname(__file__), 'config.py')
    config_content = """
import threading

_shared_resource = {
    'counter': 0
}

_resource_lock = threading.Lock()

def get_shared_resource():
    return _shared_resource

def get_resource_lock():
    return _resource_lock
"""
    with open(config_path, 'w') as f:
        f.write(config_content)

    main_path = os.path.join(os.path.dirname(__file__), 'main.py')
    process = subprocess.run(['python3', main_path], capture_output=True, text=True)
    output = process.stdout.strip()
    
    # Extract the final counter value using regex
    match = re.search(r"Final counter value: (\d+)", output)
    if match:
        return int(match.group(1)), output
    return None, output

if __name__ == "__main__":
    print("Running main.py multiple times to check for race condition...")
    
    final_counters = []
    full_outputs = []
    
    num_runs = 10 # Increased number of runs to make race condition more apparent
    expected_sum = sum(range(1, 101)) # Sum of 1 to 100

    for i in range(num_runs):
        print(f"\n--- Running Test Run {i+1} ---")
        
        counter_value, output = run_main_and_get_final_counter()
        
        final_counters.append(counter_value)
        full_outputs.append(output)
        print(output)
        
    print("\n--- Summary of Final Counter Values ---")
    print(final_counters)
    
    # Check for inconsistency (race condition)
    if len(set(final_counters)) > 1:
        print("Race condition detected: Final counter values are inconsistent!")
    else:
        print("No race condition detected in this set of runs (or values are consistently wrong).")
    
    # Check if the values are correct (sum of 1 to 100 is 5050)
    if all(c == expected_sum for c in final_counters):
        print(f"All final counter values are correct ({expected_sum}).")
    else:
        print(f"Some or all final counter values are incorrect (expected {expected_sum}).")
    
    print("\nThe agent's task will be to fix this race condition and ensure all runs consistently yield the correct sum.")
