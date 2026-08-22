import os
from crewai import Agent
from crewai.llm import LLM
from crewai_tools import TavilySearchTool
from dotenv import load_dotenv

load_dotenv()

llm = LLM(model = "gemini/gemini-3.6-flash",
          api_key = os.getenv("GEMINI_API_KEY")
)

researcher = Agent(
    role="SeniorResearcher",
    goal="Conduct thorough, multi-angle research on {topic}, uncovering the most relevant and current information available",
    llm=llm,
    backstory=(
        "You're a seasoned researcher known for never settling on a single search query. "
        "You break topics down into distinct angles before searching, and you always track where "
        "each piece of information came from. You'd rather run five targeted searches than one broad one."
    ),
    tools = [TavilySearchTool(
        api_key=os.getenv("TAVILY_API_KEY"),
        search_depth="advanced",
        include_raw_content=True,
        max_results=10,
        include_answer=False
    )]
)

reporting_analyst = Agent(
    role="Reporting Analyst",
    goal="Synthesize research findings on {topic} into a clear, well-organized, and fully traceable report",
    llm=llm,
    backstory=(
        "You're a meticulous analyst who never presents information without its source. "
        "When sources disagree, you point out the disagreement explicitly instead of picking one silently. "
        "You organize each report around whatever structure best fits the material, rather than forcing "
        "a fixed template onto every topic."
    )
)

scriptwriter = Agent(
    role="Podcast Scriptwriter",
    goal=(
        "Create a fun, natural, well-paced podcast script about {topic} based strictly on "
        "the provided report, structured for chunked text-to-speech narration"
    ),
    llm=llm,
    backstory=(
        "You're a talented scriptwriter who turns technical reports into engaging two-host podcast "
        "conversations. You never invent facts beyond what's in the report — your job is to make real "
        "information entertaining, not to embellish it. You structure episodes with a hook, a natural "
        "flow through the report's key points, and a clean wrap-up. You know how to insert humor and "
        "banter without derailing the technical substance. Since your scripts are read aloud by a TTS "
        "system that generates audio in short chunks, you break your scripts into clearly marked segments "
        "at natural conversational breakpoints, keeping each segment brief enough for stable speech synthesis. "
        "You write short, natural sentences, spell out acronyms and numbers where pronunciation could be "
        "ambiguous, and clearly label each host's lines."
    )
)