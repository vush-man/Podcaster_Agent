# 🎙️ Podcaster Agent

An AI-powered multi-agent system that automatically researches a topic, writes a podcast script, and generates narrated audio.

---

## 🚀 Overview

**Podcaster Agent** is an end-to-end Python application that demonstrates how multiple AI agents can collaborate to create podcast content. From topic research to final audio output, the entire workflow is automated using a structured agent pipeline.

---

## 🧠 How It Works

The system is divided into specialized agents:

1. **Research Agent** – Gathers information and insights on a given topic  
2. **Analysis Agent** – Converts research into a structured report  
3. **Scriptwriter Agent** – Writes a conversational, multi-speaker podcast script  
4. **Audio Generator** – Produces narrated audio using Google Gemini TTS  

All generated files are stored locally.

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
GEMINI_API_KEY_2=your_api_key_here
```

---

## ▶️ Usage

```bash
python main.py
```

Generated outputs (reports, scripts, audio) will be saved in the `outputs/` directory.

---

## 🛠 Tech Stack

- Python 3.8+
- Google Gemini (LLM + TTS)
- Multi-agent workflow architecture

---

## ⚠️ Notes

- API usage may incur costs.
- This project is experimental.

---

## 🤝 Contributing

Pull requests and suggestions are welcome.

