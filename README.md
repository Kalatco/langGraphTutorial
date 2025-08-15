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
   ollama pull llama3.1:70b
   ```

   - [deepseek-r1:14b](https://ollama.com/library/deepseek-r1) (9.0 GB): Performs better than the 5.2 GB model for complex questions.
   - [llama3.1:70b](https://ollama.com/library/llama3.1) (42 GB): Used for the email agent in this project.

   Note: The llama3.1:70b appears to work well for Tools, but it is incredibly slow due to its size. I recommend using OpenAI unless another model is found.

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
