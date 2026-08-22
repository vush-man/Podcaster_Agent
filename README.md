# 🎙️ Podcaster Agent

An AI-powered multi-agent system that researches any user-provided topic, writes a conversational podcast script, and generates narrated audio.

---

## 🚀 Overview

**Podcaster Agent** is an end-to-end Python application that demonstrates how multiple AI agents can collaborate to tranform a user-defined topic into a complete podcast.
The workflow combines web-research, AI-powered analysis, scriptwriting, and text-to-speech generation into a single automated pipeline.
Instead of relying on a predefined topic, users can now enter any topic at runtime and the system researches it using a web search tool before generating the podcast.

---

## 🧠 How It Works

The system uses specialized agents and tools for each stage of the pipeline:

1. **Research Agent** – Searches web for current information, trends, insights, and relevant sources related to the user-provided topic.
2. **Analysis Agent** – Processes the research findings and converts research into a structured an detailed report.
3. **Scriptwriter Agent** – Converts the research report into a natural, engaging, multi-speaker podcast script.
4. **Audio Generator** – Uses Google Gemini TTS to convert the generated podcast script into narrated audio.

### Workflow

```text
User enters a topic
        ↓
   Web Research
        ↓
   Research Agent
        ↓
  Analysis Agent
        ↓
 Scriptwriter Agent
        ↓
   Gemini TTS
        ↓
   Podcast Audio
```

All generated files are stored locally.

---

## ✨ Features

- 🎯 **User-defined topics** – Enter any topic when the application starts.
- 🔎 **Web-enabled research** – The Research Agent uses a web search tool to gather current information instead of relying solely on model knowledge.
- 🤖 **Multi-agent architecture** – Separate agents handle research, analysis, and scriptwriting.
- 📝 **Automated podcast scripting** – Generates conversational, multi-speaker scripts from research findings.
- 🎙️ **AI voice generation** – Converts the final script into narrated podcast audio using Google Gemini TTS.
- 📚 **Current information** – Web research allows the system to incorporate recent developments and market information.
- 💾 **Local output storage** – Generated podcast files and other outputs are stored locally.

---

## 📁 Project Structure

```
Podcaster_Agent/
├── main.py
├── agents.py
├── tasks.py
├── custom_tools.py
├── requirements.txt
├── outputs
├── .gitignore
├── .env.example
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/vush-man/Podcaster_Agent.git
cd Podcaster_Agent
pip install -r requirements.txt
```

Create a `.env` file:
```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Usage

```bash
python main.py
```

The application will prompt you to enter a topic:

```text
Enter the topic for the podcast:
```

For example:

```text
Enter the topic for the podcast: The future of AI voice agents
```

The system will then:

1. Research the topic using the web search tool.
2. Analyze the collected information.
3. Generate a podcast script.
4. Convert the script into narrated audio.
5. Save the generated files locally.

Generated outputs are stored in the `outputs/` directory.

---

## 🛠 Tech Stack

- Python 3.11
- CrewAI - Multi-agent orchestration
- Google Gemini (LLM + TTS)
- Web Search Tool - Real time topic research
- Multi-agent workflow architecture

---

## 🏗️ Architecture

The project follows a sequential multi-agent architecture:

```text
                    ┌─────────────────┐
                    │   User Topic    │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ Research Agent  │
                    │  + Web Search   │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ Analysis Agent  │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ Scriptwriter    │
                    │     Agent       │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │   Gemini TTS    │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ Podcast Audio   │
                    └─────────────────┘
```

---

## ⚠️ Notes

- API usage may incur costs depending on the configured services.
- Web search results depend on the search provider and available sources.
- The project is experimental and intended as a demonstration of multi-agent AI workflows.

---

## 🤝 Contributing

Pull requests, improvements, and suggestions are welcome.

If you experiment with the project or build additional capabilities, feel free to contribute.
