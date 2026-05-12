# AI Game Studio

A small [CrewAI](https://github.com/joaomdmoura/crewAI) project that runs a game-design crew powered by Groq. The crew produces a structured game design document (for example, a cyberpunk open-world RPG concept).

## Prerequisites

- Python 3.10+ (3.12 is used in development)
- A [Groq](https://console.groq.com/) API key

## Setup

1. Clone the repository and enter the project directory.

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with:

   - `GROQ_API_KEY` — your Groq API key (required)
   - `MODEL_NAME` — optional; used where the code loads model settings from the environment (see `agents/game_designer.py`)

## Run

```bash
python main.py
```

The script kicks off the crew and prints the final game design output to the terminal.

## Project layout

| Path | Purpose |
|------|---------|
| `main.py` | Entry point; runs the crew |
| `crews/` | Crew definitions |
| `agents/` | Agent roles and LLM configuration |
| `tasks/` | Task descriptions and expected outputs |

## Dependencies

See `requirements.txt` for pinned packages (`crewai`, `crewai-tools`, `langchain`, `langchain-groq`, `python-dotenv`, `pydantic`).

## License

Add a license file if you plan to distribute this project.
