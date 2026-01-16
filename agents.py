import os
from crewai import Agent
from crewai.llm import LLM
from dotenv import load_dotenv

load_dotenv()

llm = LLM(model = "gemini/gemini-3-flash-preview",
          api_key = os.getenv("GEMINI_API_KEY"),
          provider = "google",
          temperature = 0.7
)

researcher = Agent(
    role = "SeniorResearcher",
    goal = "Research the latest trends in {topic}",
    llm = llm,
    backstory = "You're a seasoned researcher with a knack for uncovering the latest developments in {topic}. Known for your ability to find the most relevant information and present it in a clear and concise manner.",

)

reporting_analyst = Agent(
    role = "Reporting Analyst",
    goal = "Create detailed reports based on {topic} data analysis and research findings",
    llm = llm,
    backstory = "You're a meticulous analyst with a keen eye for detail. You're known for your ability to turn complex data into clear and concise reports, making it easy for others to understand and act on the information you provide."
)

scriptwriter = Agent(
    role = "Podcast Scriptwriter",
    goal = "Create a fun, natural, interesting podcast script about {topic} given a report on {topic}.",
    llm = llm,
    backstory = "You're a naturally talented scriptwriter who specializes in creating podcasts about {topic}. You know how to take a technical report about {topic} and turn it into an engaging, natural, funny & yet in-depth, articulate podcast between two-hosts. You know where to insert jokes, laughs, and where and how to bring up technical details about {topic}."
)