#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from stockbot.crew import Stockbot

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def get_stock_name():
    """
    Prompt the user for a stock name/symbol.
    """
    print("Welcome to Stockbot - Your AI-powered stock analysis tool!")
    print("--------------------------------------------------------")
    stock_name = input("Enter the stock symbol you want to analyze (e.g., AAPL, MSFT, GOOGL): ")
    return stock_name.strip().upper() or "AAPL"  # Default to AAPL if empty input

def run():
    """
    Run the crew to analyze a stock.
    """
    stock_name = get_stock_name()
    print(f"\nAnalyzing {stock_name}. This may take a few minutes...\n")
    
    inputs = {
        'stock_name': stock_name,
    }
    
    try:
        result = Stockbot().crew().kickoff(inputs=inputs)
        print(f"\nAnalysis complete! Check the 'stock_analysis_report.md' file for the full report.")
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    stock_name = get_stock_name()
    
    inputs = {
        "stock_name": stock_name
    }
    try:
        Stockbot().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Stockbot().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    stock_name = get_stock_name()
    
    inputs = {
        "stock_name": stock_name
    }
    try:
        Stockbot().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    run()
