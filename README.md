# Simple Python Project

This is a minimal Python project setup with a `requirements` folder containing the dependency `langgraph`.

## Structure
- `requirements/requirements.txt` — Python dependencies
- `main.py` — Example entry point


## Setup
1. **Install Ollama** (for local LLM inference):
   - Download and install Ollama from [https://ollama.com/download](https://ollama.com/download)

2. **Pull required model** (run in terminal after installing Ollama):
   ```powershell
   ollama pull deepseek-r1:14b 
   ```

   Note: The deepseek-r1:14b model is 9.0 GB in size. This model works better than the 5 GB model for more complex questions.

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
