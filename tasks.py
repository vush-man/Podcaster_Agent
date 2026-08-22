import os
from crewai import Task
from agents import researcher, reporting_analyst, scriptwriter
from datetime  import datetime

os.makedirs("outputs", exist_ok=True)
research_report = f"outputs/research_report-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
report = f"outputs/report-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
podcast_script = f"outputs/podcast_script-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"

research_task = Task(
    agent=researcher,
    description=(
        "Conduct a thorough research about {topic}. The current date is {current_date} — "
        "prioritize the most recent developments and flag anything older than 6 months as background context, not current state. "
        "Do not rely on a single search query. Break {topic} down into multiple distinct angles "
        "(e.g. general overview, specific players/examples, challenges or limitations, data/statistics, "
        "recent news, or other angles relevant to this specific topic) and run a separate search for each angle. "
        "Use your judgment on which angles matter most for {topic} — not every topic needs the same categories. "
        "For every fact, statistic, or claim you record, include the source URL next to it — "
        "do not report any information without its source."
    ),
    expected_output=(
        "A list with at least 10 of the most relevant findings on {topic}, each including: "
        "summary, key details, direct excerpts (max 1-2 sentences), source URL, and publish date if available."
    ),
    output_file=research_report
)

reporting_task = Task(
    agent=reporting_analyst,
    description=(
        "Review the research context about {topic} and organize the findings into a comprehensive, structured report. "
        "Decide on sections that make sense for {topic} specifically — do not force a fixed template. "
        "For example, a market/industry topic might need sections like players, data, and challenges, "
        "while a historical or technical topic might need entirely different groupings. Use your judgment. "
        "Where sources disagree on a fact or figure, explicitly note the discrepancy and cite all conflicting "
        "sources rather than silently picking one. "
        "Preserve source URLs from the research context so every claim in the report remains traceable. "
        "Focus exclusively on {topic} — do not include tangential information."
    ),
    expected_output=(
        "A fully structured report on {topic}, organized into sections appropriate to the topic, each containing "
        "detailed findings, cited sources, and explicit notes on any conflicting data points found in the research."
    ),
    output_file=report
)

scripting_task = Task(
    agent=scriptwriter,
    description=(
        "Review the report about {topic} and write a podcast script between two hosts, **Joe** and **Jane**, "
        "who are knowledgeable about {topic} but keep the conversation fun and natural. "
        "Base all factual content strictly on the report — do not invent facts or statistics. "
        "Select the most interesting and important points from the report rather than including everything; "
        "a focused, well-paced episode is better than an exhaustive one. "
        "Structure the episode with a natural opening hook, a flowing discussion through the key points, "
        "and a clean wrap-up. Write in short, natural sentences suitable for text-to-speech narration — "
        "spell out acronyms and numbers where pronunciation could be ambiguous. "
        "Label each line clearly with the speaker's name (Joe: / Jane:). "
        "You may include brief reaction cues in parentheses (e.g. (laughs), (pause)) sparingly, "
        "but do not include sound effect directions that a TTS engine cannot produce. "
        "Break the script into natural segments at topic transitions or natural pauses in conversation. "
        "Mark the start of each segment with a line like '[SEGMENT: short title]' before that segment's dialogue. "
        "Keep each segment short enough to speak in under 2-3 minutes to stay within "
        "TTS quality limits — do not let any single segment run long."
    ),
    expected_output=(
        "A complete podcast script about {topic}, broken into [SEGMENT: ...] blocks, "
        "with clear speaker labels (Joe: / Jane:), grounded in the report, TTS-ready,"
        "with occasional natural reaction cues but no unproducible sound effect directions."
    ),
    output_file=podcast_script
)