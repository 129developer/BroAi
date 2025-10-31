import os
from dotenv import load_dotenv
from broai.core.graph import create_broai_graph

# Load environment variables from .env file
load_dotenv()

def main():
    """
    Main entry point for the BroAi agent.
    Runs a pre-defined task through the LangGraph.
    """
    print("Initializing BroAi Agent...")

    # Check for required API keys
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in .env file. Please set it in the .env file.")
        return

    # Create and compile the LangGraph
    app = create_broai_graph()

    # --- Pre-defined Task Execution ---
    task_prompt = "Find the current stock price of NVIDIA and write a new tool to calculate its 7-day moving average."
    print(f"\n--- Running Pre-defined Task ---\nTask: {task_prompt}")

    inputs = {"messages": [("user", task_prompt)]}

    # Stream the execution of the graph
    final_output = None
    for output in app.stream(inputs):
        for key, value in output.items():
            print(f"Output from node '{key}': {value}")
            final_output = value

    print("\n--- Task Execution Complete ---")
    if final_output and "messages" in final_output:
        print("Final Agent Response:")
        print(final_output["messages"][-1])
    # -----------------------------------

if __name__ == "__main__":
    main()
