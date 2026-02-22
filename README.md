# OpenHands Demo: Beyond the IDE

This repository contains a comprehensive demonstration of OpenHands, an open-source, model-agnostic platform for autonomous AI-driven software development. The demo showcases three distinct form factors of OpenHands and highlights how it differentiates from traditional AI-assisted IDEs like Cursor and Claude Code.

## Overview

OpenHands is not just another AI coding assistant. It is a **full-fledged platform** for building, deploying, and scaling autonomous software engineering agents. While tools like Cursor and Claude Code serve as co-pilots within your development environment, OpenHands operates as an autonomous platform that can work independently, integrate into CI/CD pipelines, and scale across thousands of agents.

### Key Differentiators

| Feature | Cursor / Claude Code | OpenHands |
| :--- | :--- | :--- |
| **Nature** | AI-Assisted IDE / CLI | Autonomous Agentic Platform |
| **Autonomy** | Human-in-the-loop | High autonomy with oversight |
| **Model Lock-in** | Often proprietary | Fully model-agnostic |
| **Deployment** | Desktop only | Local, Cloud, Enterprise, K8s |
| **Extensibility** | Limited plugins | Programmatic SDK |
| **Scalability** | Single-user | 1000s of parallel agents |

## Demo Structure

This repository contains three distinct demos, each showcasing a different form factor and use case of OpenHands:

### 1. CLI Demo: The Autonomous Bug Hunter ⚙️

**Location:** `cli_demo/`

**Scenario:** An OpenHands agent autonomously identifies, reproduces, and fixes a complex race condition in a multi-threaded Python application.

**Key Message:** Autonomy and reliability in headless environments, perfect for CI/CD pipelines.

**How to Run:**
```bash
cd cli_demo
python3 test_race_condition.py
```

**Files:**
- `main.py`: The target application with a race condition
- `utils.py`: Utility functions demonstrating the race condition
- `config.py`: Configuration and shared resources
- `test_race_condition.py`: Test script to demonstrate the bug and verify the fix
- `cli_demo_script.md`: Narrated script for the demo

### 2. Web Demo: The Full-Stack Feature Architect 🌐

**Location:** `web_demo/`

**Scenario:** An OpenHands agent researches a public API, understands its documentation, and integrates it into a live web application.

**Key Message:** Visibility, multi-modal interaction (browser + code editor), and collaborative development.

**How to Run:**
1. Open `web_demo/index.html` in your web browser
2. The page will fetch and display a random joke from a public API

**Files:**
- `index.html`: The main HTML page
- `style.css`: CSS styling
- `script.js`: JavaScript for API integration
- `web_demo_script.md`: Narrated script for the demo

### 3. SDK Demo: The Agentic Infrastructure 🔧

**Location:** `sdk_demo/`

**Scenario:** A Python script instantiates a "Security Sentinel" agent that scans and refactors code, demonstrating how OpenHands can be embedded into custom workflows.

**Key Message:** Embeddability and scalability. OpenHands isn't just a tool you use; it's a component you build with.

**How to Run:**
```bash
cd sdk_demo
python3 sdk_agent.py
```

**Files:**
- `target_file.py`: The target file to be scanned and modified
- `sdk_agent.py`: Simulated OpenHands agent demonstrating the SDK
- `sdk_demo_script.md`: Narrated script for the demo

## Main Landing Page

**File:** `index.html`

A comprehensive landing page that ties all three demos together, explains the differentiation from other AI tools, and provides an overview of OpenHands' capabilities.

**To View:** Open `index.html` in your web browser.

## Understanding the Demos

### What Makes OpenHands Different?

1. **True Autonomy:** OpenHands agents can plan complex tasks, execute them independently, and verify their own work. Unlike Cursor or Claude Code, which require continuous human guidance, OpenHands operates as a true autonomous agent.

2. **Model Agnosticism:** Works with any LLM—Claude, GPT-4, Llama, Qwen, and more. Never locked into a single model provider.

3. **Open Source & Extensible:** Fully open-source (MIT licensed) with a programmatic SDK for custom tools and capabilities.

4. **Deployment Flexibility:** Run locally, in the cloud, or in your own VPC. Integrate into Docker, Kubernetes, or any infrastructure.

5. **Scalability:** Orchestrate thousands of agents in parallel for large-scale tasks like refactors, security audits, or dependency updates.

### The "Wow" Factor

- **CLI Demo:** Watch an agent autonomously fix a multi-file race condition with zero human intervention, then verify the fix is correct.
- **Web Demo:** Observe the agent opening a real browser, reading documentation, and writing code—all in one integrated interface.
- **SDK Demo:** See how just a few lines of Python code can instantiate a powerful agent and integrate it into your CI/CD pipeline.

## Quick Start

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yang0733/openhands-demo.git
   cd openhands-demo
   ```

2. **Explore the Landing Page:**
   ```bash
   # Open index.html in your browser
   open index.html  # macOS
   # or
   xdg-open index.html  # Linux
   # or
   start index.html  # Windows
   ```

3. **Run the CLI Demo:**
   ```bash
   cd cli_demo
   python3 test_race_condition.py
   ```

4. **Run the Web Demo:**
   ```bash
   # Open web_demo/index.html in your browser
   open web_demo/index.html
   ```

5. **Run the SDK Demo:**
   ```bash
   cd sdk_demo
   python3 sdk_agent.py
   ```

## Learn More

- **OpenHands Official Website:** https://openhands.dev/
- **OpenHands Documentation:** https://docs.openhands.dev/
- **OpenHands GitHub Repository:** https://github.com/OpenHands/OpenHands

## About OpenHands

OpenHands is an open-source platform for building, evaluating, and deploying AI agents that interact with digital environments. It is designed to be model-agnostic, scalable, and extensible, enabling developers to create custom agentic solutions for a wide range of software engineering tasks.

## License

This demo repository is provided as-is for educational and demonstration purposes. OpenHands itself is licensed under the MIT License.

## Contributing

We welcome contributions and feedback! If you have suggestions for improving this demo or want to add new scenarios, please feel free to open an issue or submit a pull request.

---

**Disclaimer:** This is a demonstration repository created to showcase the capabilities of OpenHands. The agents demonstrated here are simplified simulations for illustrative purposes. Real-world OpenHands agents are more sophisticated and capable of handling complex, real-world software engineering tasks.
