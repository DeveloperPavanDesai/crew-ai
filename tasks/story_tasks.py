from crewai import Task
from agents.story_writer import story_writer_agent

story_task = Task(
    description="""
    Create a rich and immersive story
    for a cyberpunk open-world RPG game.

    Include:
    - Main protagonist
    - Main conflict
    - Factions
    - World history
    - Major story arcs
    - Emotional themes
    - Plot twists
    - Ending possibilities
    """,

    expected_output="""
    A detailed narrative design document
    with lore, factions, conflicts,
    and cinematic storytelling.
    """,

    agent=story_writer_agent
)