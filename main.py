import os
from crewai import Crew, Process
from agents import researcher, reporting_analyst, scriptwriter
from tasks import research_task, reporting_task, scripting_task
from datetime import datetime
from custom_tools import gemini_voice_tool

topic = input("Enter the topic for the podcast: ")
try:
    crew = Crew(
        agents = [researcher, reporting_analyst, scriptwriter],
        tasks = [research_task, reporting_task, scripting_task],
        verbose = True,
        process = Process.sequential
    )

    inputs = {
            'topic': topic,
            'current_month': str(datetime.now().month),
            'current_year': str(datetime.now().year)
        }

    result = crew.kickoff(inputs = inputs)
    script = result.tasks_output[2].raw 
except Exception as e:
    print(f"Crew execution failed: {e}")
    print("Using existing podcast script instead...")
    with open('podcast_script.md', 'r') as f:
        script = f.read()

print("\nGenerating audio from podcast script...")
audio_file = gemini_voice_tool(script=script)
print(f"Audio file created: {audio_file}")