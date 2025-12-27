from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, SeleniumScrapingTool
from dotenv import load_dotenv

load_dotenv()

#tools
web_search_tool = SerperDevTool()
web_scrape_tool = ScrapeWebsiteTool()
selenium_scrape_tool = SeleniumScrapingTool()

toolkit = [web_search_tool, web_scrape_tool, selenium_scrape_tool]


@CrewBase
class MarketResearchCrew():
	"""MarketResearchCrew crew"""
	agents: List[BaseAgent]
	tasks:List[Task]

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# agents

	@agent
	def market_research_specialist(self) -> Agent:
		"""Market Research Specialist agent"""
		return Agent(
			config = self.agents_config['market_research_specialist'],
			tools = toolkit
		)

	@agent
	def competitive_inteligence_analyst(self) -> Agent:
		"""Competitive Intelligence Analyst agent"""
		return Agent(
			config = self.agents_config['competitive_inteligence_analyst'],
			tools = toolkit
		)
	
	@agent
	def customer_insights_researcher(self) -> Agent:
		"""Customer Insights Researcher agent"""
		return Agent(
			config = self.agents_config['customer_insights_researcher'],
			tools = toolkit
		)

	@agent
	def product_strategy_advisor(self) -> Agent:
		"""Product Strategy Advisor agent"""
		return Agent(
			config = self.agents_config['product_strategy_advisor'],
			tools = toolkit
		)

	@agent
	def business_analyst(self) -> Agent:
		"""Business Analyst agent"""
		return Agent(
			config = self.agents_config['business_analyst'],
			tools = toolkit
		)


	# tasks
	@task
	def market_resear_task(self) -> Task:
		"""Market Research Task"""
		return Task(
			config = self.tasks_config['market_resear_task']
		)

	@task
	def competitive_inteligence_task(self) -> Task:
		"""Competitive Intelligence Task"""
		return Task(
			config = self.tasks_config['competitive_inteligence_task'],
			context =[self.market_resear_task()]
		)

	@task
	def customer_insights_task(self) -> Task:
		"""Customer Insights Task"""
		return Task(
			config = self.tasks_config['customer_insights_task'],
			context= [self.market_resear_task(), self.competitive_inteligence_task()]
		)

	@task
	def product_strategy_task(self) -> Task:
		"""Product Strategy Task"""
		return Task(
			config = self.tasks_config['product_strategy_task'],
			context= [self.market_resear_task(),self.competitive_inteligence_task(), self.customer_insights_task()]
		)

	@task
	def business_analysis_task(self) -> Task:
		"""Business Analysis Task"""
		return Task(
			config = self.tasks_config['business_analysis_task'],
			context= [self.market_resear_task(),self.competitive_inteligence_task(), self.customer_insights_task(), self.product_strategy_task()],
			output_file = 'output/final_report.md'
		)


	@crew
	def crew(self)-> Crew:
		return Crew(
			agents=self.agents,
			tasks=self.tasks
		)
	
	

