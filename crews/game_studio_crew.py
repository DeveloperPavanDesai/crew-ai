from crewai import Crew
from tasks.game_design_tasks import game_design_task
from agents.game_designer import game_designer_agent
from agents.story_writer import story_writer_agent
from tasks.story_tasks import story_task

game_studio_crew = Crew(
    agents=[game_designer_agent, story_writer_agent],
    tasks=[game_design_task, story_task],
    verbose=True,
)