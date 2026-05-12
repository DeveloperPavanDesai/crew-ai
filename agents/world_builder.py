from crewai import Agent, LLM
from config import llm

world_builder_agent = Agent(
    role="Open World Architect",

    goal="""
    Create immersive game worlds,
    cities, regions, environments,
    ecosystems, and exploration systems.
    """,

    backstory="""
    You are a legendary open-world designer
    responsible for building massive cities,
    dynamic ecosystems, environmental storytelling,
    and immersive exploration experiences.
    """,

    verbose=True,

    llm=llm
)