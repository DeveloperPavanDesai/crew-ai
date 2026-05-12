from crewai import Crew
from tasks.game_design_tasks import game_design_task
from agents.game_designer import game_designer_agent

game_studio_crew = Crew(
    agents=[game_designer_agent],
    tasks=[game_design_task],
    verbose=True,
)
