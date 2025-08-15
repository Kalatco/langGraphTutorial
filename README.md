# Simple Python Project

## About This Project
This project is based on the tutorial from Real Python:
[LangGraph: Build State Machines for LLM Applications in Python](https://realpython.com/langgraph-python/)

This is a minimal Python project setup with a `requirements` folder containing the dependency `langgraph`.

## Structure
- `requirements/requirements.txt` — Python dependencies
- `main.py` — Example entry point


## Setup
1. **Install Ollama** (for local LLM inference):
   - Download and install Ollama from [https://ollama.com/download](https://ollama.com/download)


2. **Pull required models** (run in terminal after installing Ollama):
   ```powershell
   ollama pull deepseek-r1:14b
   ```

   - [deepseek-r1:14b](https://ollama.com/library/deepseek-r1) (9.0 GB): Performs better than the 5.2 GB model for complex questions.

   Note: Azure OpenAI was used for the email agent because other Ollama models did not provide adequate results for this use case.

3. **Create a virtual environment** (optional but recommended):
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

4. **Install dependencies:**
   ```powershell
   pip install -r requirements/requirements.txt
   ```

5. **Run the example:**
   ```powershell
   python main.py
   ```
