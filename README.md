# Podcaster - AI-Powered Podcast Generation

An intelligent podcast generation system that automates the creation of engaging podcast scripts and audio content using AI agents. The system researches topics, analyzes findings, and generates natural, entertaining podcast scripts with multi-speaker audio output.

## Features

- **Automated Research**: Uses AI agents to conduct thorough research on specified topics
- **Report Generation**: Creates comprehensive reports based on research findings
- **Script Writing**: Generates engaging podcast scripts with dialogue between two hosts
- **Audio Generation**: Converts podcast scripts to multi-speaker audio using Google Gemini's text-to-speech capabilities
- **Multi-Agent System**: Leverages CrewAI framework with specialized agents (Researcher, Reporting Analyst, Scriptwriter)

## Project Structure

```
├── main.py                 # Entry point - orchestrates the entire pipeline
├── agents.py              # Defines AI agents (Researcher, Analyst, Scriptwriter)
├── tasks.py               # Defines tasks for each agent
├── custom_tools.py        # Custom tools including voice generation
├── outputs               # Generated outputs (research reports, scripts, audio)
└── requirements.txt       # Project dependencies
```

## How It Works

1. **Research Phase**: The Researcher agent gathers the latest trends and information about the specified topic
2. **Analysis Phase**: The Reporting Analyst synthesizes research findings into a detailed report
3. **Script Generation**: The Scriptwriter creates an engaging podcast script with dialogue between two hosts (Joe and Jane)
4. **Audio Production**: The system converts the podcast script to multi-speaker audio using Google Gemini's TTS

## Installation

1. Clone or download the project
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables in a `.env` file:
   ```
   GEMINI_API_KEY=your_gemini_api_key
   GEMINI_API_KEY_2=your_gemini_api_key_for_tts
   ```

## Usage

Run the main script to generate a podcast:

```bash
python main.py
```

This will:
1. Research the configured topic (default: "AI automation related problems that companies are actively paying external people to solve")
2. Generate a research report
3. Create a comprehensive analysis report
4. Write a podcast script
5. Convert the script to audio with multi-speaker voices

All outputs are saved to the `outputs/` directory with timestamps.

## Configuration

The default topic and behavior can be modified in `main.py`:

```python
inputs = {
    'topic': 'Your desired topic here',
    'current_month': str(datetime.now().month),
    'current_year': str(datetime.now().year)
}
```

## Output Files

Generated files are saved in the `outputs/` directory:
- `research_report-{timestamp}.md` - Research findings
- `report-{timestamp}.md` - Analysis report
- `podcast_script-{timestamp}.md` - Podcast script with dialogue
- `podcast-{timestamp}.wav` - Generated audio file

## Requirements

- Python 3.8+
- Google Gemini API key (for LLM and TTS)
- CrewAI framework
- Google GenAI SDK

See `requirements.txt` for all dependencies and versions.

## API Keys

You'll need valid Google Gemini API keys:
- `GEMINI_API_KEY`: For the main LLM operations
- `GEMINI_API_KEY_2`: For text-to-speech audio generation (can use the same key)

Get your API keys from [Google AI Studio](https://aistudio.google.com/)

## Error Handling

If the crew execution fails for any reason, the system will attempt to use an existing `podcast_script.md` file as a fallback.

## Future Enhancements

- Support for custom voice configurations
- Multiple topic batching
- Customizable podcast length and style
- Support for additional TTS providers
- Integration with podcast hosting platforms

## License

Not specified

## Contributing

Feel free to extend and modify the agents, tasks, and tools to customize the podcast generation process for your needs.

