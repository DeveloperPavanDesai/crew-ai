from crewai import Agent, LLM
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(
    model=os.getenv("MODEL_NAME"),
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.7,
)

story_writer_agent = Agent(

    role = "Senior Narrative Designer",

    goal = """
    Create emotionally engaging and immersive
    video game stories with compelling lore,
    characters, factions, and plot twists.
    """,

    backstory="""
    You are an award-winning narrative designer
    known for writing deep RPG stories,
    branching narratives, emotional character arcs,
    dystopian worlds, and cinematic storytelling.
    """,

    verbose=True,

    llm=llm
)