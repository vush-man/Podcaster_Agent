import os
from crewai import Task
from agents import researcher, reporting_analyst, scriptwriter
from datetime  import datetime

os.makedirs("outputs", exist_ok=True)
research_report = f"outputs/research_report-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
report = f"outputs/report-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
podcast_script = f"outputs/podcast_script-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"

research_task = Task(
    agent = researcher,
    description = "Conduct a thorough research about {topic}. Make sure you find any interesting and relevant information given the current date is {current_month} {current_year}.",
    expected_output = "A list with atleast10 most relevant news & progress on {topic} with summary, details, excerpts, and more",
    output_file = research_report
)

reporting_task = Task(
    agent = reporting_analyst,
    description = "Review the research context about {topic} and organize the findings into a comprehensive report about {topic}. Make sure the report is detailed and contains any and all relevant information about {topic}.Focus the report exclusively on {topic}",
    expected_output = "A fully fledged report about {topic} with the main topics and findings, each with a full section of information.",
    output_file = report
)

scripting_task = Task(
    agent = scriptwriter,
    description = "Review the report about {topic} and write an elaborate podcast script between two hosts who are knowledgable about {topic} and yet are fun on podcast. **Joe** and **Jane** are the speakers, give them dialogues by name.",
    expected_output = "A full podcast script about {topic} with speaker labels, sound effects, laughs, silences, and every last bit of details.",
    output_file = podcast_script
)