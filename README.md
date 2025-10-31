# BroAi: Self-Learning, Self-Updating AI Agent

**BroAi** is a cutting-edge, self-learning, and self-updating AI agent built on the **LangGraph** framework. It is designed to handle complex tasks through **multi-agent planning** and possesses the unique ability to **write new tools and use them** dynamically to solve novel problems.

## Features

*   **LangGraph Core:** Utilizes LangGraph for robust state management and complex agent orchestration.
*   **Multi-Agent Planning:** Employs specialized agents for planning, execution, and tool creation.
*   **Self-Updating:** Can analyze its own failures and write/integrate new tools to improve performance.
*   **Common Tooling:** Pre-configured to integrate with popular LLM providers and search APIs.
*   **Full Production Setup:** Includes Docker, CI/CD workflows, testing framework, and comprehensive documentation scaffolding.

## Getting Started

### Prerequisites

*   Python 3.10+
*   `make` (optional, for convenience)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/129developer/BroAi.git
    cd BroAi
    ```

2.  **Set up your environment:**
    Create a `.env` file and fill in your API keys.
    ```bash
    cp .env.example .env # (The .env file is already created but this is a common practice)
    # Edit .env with your keys
    ```

3.  **Install dependencies:**
    ```bash
    make install
    # or
    # pip install -r requirements.txt
    ```

## Development

*   **Run the agent:** `make run`
*   **Run tests:** `make test`
*   **Lint code:** `make lint`
*   **Format code:** `make format`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
