from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List, ClassVar
from pydantic import ConfigDict
from pathlib import Path
from .tools.custom_tool import custom_search

tools = [custom_search] 

@CrewBase
class ResearchAndBlogCrew():
	"""ResearchAndBlog crew"""
	
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# to define agents, in case of agent orders does not matter.
	@agent
	def report_generator(self) -> Agent:
		return Agent(
			config = self.agents_config['report_generator'],
			tools = tools
		)

	@agent
	def blog_writer(self) -> Agent:
		return Agent(
			config = self.agents_config['blog_writer'],
			tools = tools
		)
	
	# to define tasks, order needs to be maintained because order of task matters.
	@task
	def report_task(self) -> Task:
		return Task(
			config = self.tasks_config['report_task']
		)
	@task
	def blog_writing_task(self) -> Task:
		return Task(
			config = self.tasks_config['blog_writing_task'],
			output_file = 'blog/blog_post.md'
		)

	# crew 

	@crew
	def crew(self) -> Crew:
		return Crew(
			agents = self.agents,
			tasks = self.tasks,
			process = Process.sequential,
			verbose = True
		)

	