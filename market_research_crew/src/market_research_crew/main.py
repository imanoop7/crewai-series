#!/usr/bin/env python
import sys
import warnings

from market_research_crew.crew import MarketResearchCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        "product_idea" : "A mobile app that helps users track their daily water intake and provides personalized hydration reminders.",
    }
    try:
        MarketResearchCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        print(f"An error occurred while running the crew: {e}", file=sys.stderr)

