from crewai import Task
from agents.game_designer import game_designer_agent

game_design_task = Task(
    description="""
    Create a detailed concept for a cyberpunk open-world RPG game.

    Include:
    - Game title
    - Genre
    - Core gameplay loop
    - Main gameplay mechanics
    - Progression system
    - Story premise
    - Unique features
    - Monetization model
    """,

    expected_output="""
    A professional and structured game design document
    describing the complete game concept.
    """,

    agent=game_designer_agent,
)