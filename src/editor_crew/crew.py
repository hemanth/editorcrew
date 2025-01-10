from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class EditorCrew():
	"""EditorCrew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

    # Agents
	@agent
	def content_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['content_writer'],
			verbose=True
		)

	@agent
	def content_critic(self) -> Agent:
		return Agent(
			config=self.agents_config['content_critic'],
			verbose=True
		)
	
	@agent
	def content_editor(self) -> Agent:
		return Agent(
			config=self.agents_config['content_editor'],
			verbose=True
		)
	
	@agent
	def content_rater(self) -> Agent:
		return Agent(
			config=self.agents_config['content_rater'],
			verbose=True
		)


	# Tasks
	@task
	def writing_task(self) -> Task:
		return Task(
			config=self.tasks_config['writing_task'],
		)
	
	@task
	def critique_task(self) -> Task:
		return Task(
			config=self.tasks_config['critique_task'],
		)
	
	@task
	def editing_task(self) -> Task:
		return Task(
			config=self.tasks_config['editing_task'],
		)
	
	@task
	def rating_task(self) -> Task:
		return Task(
			config=self.tasks_config['rating_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the EditorCrew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
		)
