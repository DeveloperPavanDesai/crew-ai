from crewai import Task
from agents.character_designer import character_designer_agent

character_task = Task(
    description="""
    Design the main characters
    for a cyberpunk RPG game.

    Include:
    - Main hero
    - Main villain
    - Side characters
    - Faction leaders
    - Character abilities
    - Personality traits
    - Backstories
    - Visual design ideas
    """,

    expected_output="""
    A structured character design document
    describing all major characters,
    their personalities, motivations,
    and gameplay relevance.
    """,

    agent=character_designer_agent
)