from crewai import Task
from agents.world_builder import world_builder_agent

world_task = Task(
    description="""
    Design an immersive cyberpunk game world.

    Include:
    - Main city
    - Districts
    - Underground regions
    - Faction-controlled territories
    - Environmental storytelling
    - Exploration mechanics
    - Weather systems
    - Economy and society
    """,

    expected_output="""
    A professional world-building document
    describing environments, geography,
    exploration systems, and world atmosphere.
    """,

    agent=world_builder_agent
)