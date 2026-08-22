import os, glob
from crewai import Crew, Process
from agents import researcher, reporting_analyst, scriptwriter
from tasks import research_task, reporting_task, scripting_task
from datetime import datetime
from custom_tools import build_full_podcast

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
            'current_date': datetime.now().strftime("%B %d, %Y")
        }

    result = crew.kickoff(inputs = inputs)
    script = result.tasks_output[2].raw 
except Exception as e:
    print(f"Crew execution failed: {e}")
    print("Using existing podcast script instead...")
    existing_scripts = sorted(glob.glob("outputs/podcast_script-*.md"))
    if not existing_scripts:
        raise RuntimeError("No previous podcast script found to fall back on.") from e
    with open(existing_scripts[-1], 'r') as f:
        script = f.read()

print("\nGenerating audio from podcast script...")
audio_file = build_full_podcast(script_text=script)
print(f"Audio file created: {audio_file}")