# OpenHands SDK Demo: The Agentic Infrastructure

## Introduction (Narrator)

"Welcome to the OpenHands SDK demo. This is where the true power and extensibility of OpenHands are revealed. While the CLI and Web UI provide direct interfaces for interacting with agents, the SDK allows you to **programmatically integrate autonomous agents** into any application, workflow, or infrastructure. This transforms OpenHands from a tool you use into a component you build with, enabling a new era of agent-driven development."

"Our scenario here is a simplified 'Security Sentinel' agent. Imagine a continuous integration/continuous deployment (CI/CD) pipeline where, upon every code commit, an OpenHands agent automatically scans for specific patterns (simulating vulnerabilities or outdated code) and applies refactorings or fixes. This demonstrates how easily agentic capabilities can be embedded into existing DevOps workflows."

## Step 1: The Target Codebase (Live Demo - Show `target_file.py`)

"We have a simple Python file, `target_file.py`, which contains some 'legacy' code. Our simulated Security Sentinel agent will be tasked with refactoring an `old_function` to `new_secure_function`, an `OldClass` to `SecureClass`, and updating a version string."

*(Display the initial content of `target_file.py`.)*

```python
# This is a target file for the SDK demo.

def old_function():
    print("This is an old function.")

class OldClass:
    def __init__(self):
        self.version = "1.0"

# Some other code
def another_function():
    pass
```

## Step 2: Orchestrating the Agent with the SDK (Live Demo - Show `sdk_agent.py`)

"Now, let's look at `sdk_agent.py`. This Python script demonstrates how you would use the OpenHands SDK to instantiate and control an agent. In a real-world scenario, this script could be part of a larger CI/CD pipeline, a custom IDE extension, or a backend service."

*(Display `sdk_agent.py`, highlighting the `SimulatedOpenHandsAgent` class and its `run_task` method. Explain that in a real SDK, these would be actual OpenHands API calls.)*

```python
import os
import time

class SimulatedOpenHandsAgent:
    def __init__(self, name="SecuritySentinel"):
        self.name = name
        print(f"Simulated OpenHands Agent \033[34m{self.name}\033[0m initialized.")

    def run_task(self, task_description, target_file):
        print(f"\nAgent \033[34m{self.name}\033[0m received task: \033[33m\'{task_description}\'\033[0m on file \033[32m{target_file}\033[0m")
        time.sleep(1)
        print("Agent is analyzing the task and target file...")
        time.sleep(1)

        if not os.path.exists(target_file):
            print(f"\033[31mError: Target file {target_file} not found.\033[0m")
            return False

        print(f"Reading content of \033[32m{target_file}\033[0m...")
        with open(target_file, "r") as f:
            content = f.read()
        print("Original content:")
        print("""\n""" + content + """\n""")
        time.sleep(1)

        print("Agent is identifying vulnerabilities/refactoring opportunities...")
        time.sleep(2)

        # Simulate fixing a vulnerability or refactoring
        new_content = content.replace("old_function", "new_secure_function")
        new_content = new_content.replace("OldClass", "SecureClass")
        new_content = new_content.replace("version = \"1.0\"", "version = \"2.0-secure\"")

        if new_content != content:
            print("Agent found issues and is applying fixes/refactorings...")
            time.sleep(2)
            with open(target_file, "w") as f:
                f.write(new_content)
            print(f"\033[32mSuccessfully updated {target_file}.\033[0m")
            print("New content:")
            print("""\n""" + new_content + """\n""")
            return True
        else:
            print("\033[32mNo changes needed or no vulnerabilities found.\033[0m")
            return False

if __name__ == "__main__":
    agent = SimulatedOpenHandsAgent()
    target_file_path = "target_file.py"
    task = "Refactor \'old_function\' to \'new_secure_function\' and \'OldClass\' to \'SecureClass\', and update version to \'2.0-secure\'."
    
    # Ensure the target file is in its original state for the demo
    original_target_content = """# This is a target file for the SDK demo.\n\ndef old_function():\n    print(\"This is an old function.\")\n\nclass OldClass:\n    def __init__(self):\n        self.version = \"1.0\"\n\n# Some other code\ndef another_function():\n    pass\n"""
    with open(target_file_path, "w") as f:
        f.write(original_target_content)

    agent.run_task(task, target_file_path)

    print("\n--- SDK Demo Complete ---")
    print("The agent has completed its simulated task. You can inspect \'target_file.py\' to see the changes.")
```

## Step 3: Executing the Agent (Live Demo - Run `sdk_agent.py`)

"Now, let's run our `sdk_agent.py` script. Observe how the agent processes the task and modifies the `target_file.py`."

```bash
python3 sdk_demo/sdk_agent.py
```

*(Expected Output: The script will print messages indicating the agent's progress and the changes made to `target_file.py`.)*

## Step 4: Verifying the Changes (Live Demo - Show `target_file.py` again)

"The agent has completed its task. Let's re-examine `target_file.py` to confirm the refactorings."

*(Display the modified content of `target_file.py`.)*

```python
# This is a target file for the SDK demo.

def new_secure_function():
    print("This is an old function.")

class SecureClass:
    def __init__(self):
        self.version = "2.0-secure"

# Some other code
def another_function():
    pass
```

"As you can see, the agent successfully refactored the function name, class name, and updated the version string. This was all done programmatically, demonstrating how OpenHands agents can be integrated into automated systems to perform complex code modifications."

## Conclusion (Narrator)

"This SDK demo illustrates that OpenHands is more than just an AI assistant; it's a powerful platform for building and deploying autonomous software engineering agents. By providing a robust SDK, OpenHands empowers developers to create custom agentic solutions, automate complex workflows, and scale their engineering capabilities far beyond what traditional AI-assisted IDEs can offer. It's about building the next generation of intelligent, self-managing software systems."
