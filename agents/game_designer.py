from crewai import Agent, LLM
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(
    model=os.getenv("MODEL_NAME"),  
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.7,
)

game_designer_agent = Agent(
    role="Senior Game Designer",

    goal = """
    Create innovative and engaging game concepts
    with unique gameplay mechanics and immersive experiences.
    """,

    backstory="""
    You are a veteran AAA game designer with 15 years
    of experience designing RPGs, open-world games,
    sci-fi adventures, and multiplayer systems.
    You specialize in designing addictive gameplay loops
    and creative game worlds.
    """,

    verbose=True,

    llm="groq/llama-3.3-70b-versatile"
)