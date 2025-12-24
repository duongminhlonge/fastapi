FastAPI Project

This guide will help you **set up a virtual environment**, install dependencies, and run your FastAPI app using Uvicorn.

---

## 1. Prepare the environment

### 1.1. Create a virtual environment (if not already created)
```bash
# Create a virtual environment named "venv"
python -m venv venv
```

### 1.2. Activate the virtual environment
```bash
source venv/bin/activate
```

## 2. Install dependencies
```bash
pip install fastapi uvicorn
```
- If you have a requirements.txt file:
```bash
pip install -r requirements.txt
```

- After installing all required packages (e.g., FastAPI, Uvicorn, Black), save them to `requirements.txt` so others can install the same dependencies:
```bash
pip freeze > requirements.txt
```

## 3. Sample Project Structure
```bash
fastapi_project/
├─ venv/
├─ app/
│  ├─ __init__.py
│  ├─ main.py
│  └─ api/
│     ├─ __init__.py
│     └─ v1/
│        ├─ __init__.py
│        └─ routes.py
```
## 4. Run the FastAPI App
- Navigate to the project root directory (fastapi_project/):
```bash
cd /path/to/fastapi_project
```
- Run Uvicorn:
```bash
uvicorn app.main:app --reload
```
- Open in browser:
```bash
http://127.0.0.1:8000
```
- Swagger API docs:
```bash
http://127.0.0.1:8000/docs
```

## 5. Install Black and Flake8 (Format code PEP8)
```bash
# Install Black for auto-formatting
pip install black

# Install Flake8 for linting
pip install flake8
```

- Format code with Black
```bash
black .
```

- Check code style with Flake8
```bash
flake8 app/
```