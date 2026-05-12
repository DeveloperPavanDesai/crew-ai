from crewai import Crew, Process

from agents.game_designer import game_designer_agent
from agents.story_writer import story_writer_agent
from agents.character_designer import character_designer_agent
from agents.world_builder import world_builder_agent

from tasks.game_design_tasks import game_design_task
from tasks.story_tasks import story_task
from tasks.character_tasks import character_task
from tasks.world_tasks import world_task

game_studio_crew = Crew(
    agents=[
        game_designer_agent,
        story_writer_agent,
        character_designer_agent,
        world_builder_agent
    ],

    tasks=[
        game_design_task,
        story_task,
        character_task,
        world_task
    ],

    process=Process.sequential,

    verbose=True
)