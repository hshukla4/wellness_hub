# 🧘 Wellness Hub – Project Setup & Commands Guide

This guide provides all commands and context needed to install, maintain, and run the **Wellness Hub** AI engine project.

---

## 📦 Installing Packages in the Virtual Environment

```bash
python3 -m venv venv           # Create virtual environment in ./venv folder
source venv/bin/activate       # Activate venv (macOS/Linux)
```

# For Windows:
# .\venv\Scripts\activate


To install necessary packages listed in your `requirements.txt`:

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

To clean up and regenerate only the packages your code actually imports:

```bash
pip freeze > requirements.txt
pipreqs app --force --savepath cleaned_requirements.txt
```

> ✅ `pipreqs` strips out unused dependencies and writes only used ones to `cleaned_requirements.txt`.

---

## 🧪 Separating Development Dependencies

To avoid installing dev-only packages (e.g., `black`, `pytest`) during production deployments:

1. If you had previously installed dev tools via `requirements.txt`, uninstall them:

```bash
pip uninstall black flake8 pytest pre-commit mypy isort pylint -y
```

2. Then install them separately:

```bash
pip install -r requirements-dev.txt
```

---

## 📦 Prerequisite: Install GNU Make

Mac:
  brew install make

Linux:
  sudo apt install make

Windows:
  Use WSL or Git Bash with make installed

## 🧰 Makefile Commands

These make your workflow easier with consistent shortcuts:

| Command         | Description                                 |
|----------------|---------------------------------------------|
| `make install` | Installs the package in editable mode       |
| `make run`     | Runs the project (currently planner.py)     |
| `make test`    | Runs all tests in the project               |
| `make clean`   | Cleans up compiled files and caches         |
| `make build`   | Builds the project                          |
| `make deploy`  | Deploys the application                     |
| `make start`   | Starts the app                              |
| `make stop`    | Stops the app                               |
| `make restart` | Restarts the app                            |
| `make status`  | Shows current app status                    |
| `make logs`    | Shows log output                            |
| `make help`    | Shows Makefile help                         |
| `make version` | Displays the current version                |

---

## ✅ Editable Installation

After `make install`, you may see:

```
Successfully installed wellness_hub-0.1.0
```

This means your package was installed in **editable mode** using:

```bash
pip install -e .
```

### 🔍 Where It’s Installed

If you're in a virtual environment, it's linked from:

```
/Users/himanshushukla/projects/wellness_hub/venv/lib/python3.11/site-packages/wellness_hub.egg-link
```

And that `.egg-link` points back to your source:

```
/Users/himanshushukla/projects/wellness_hub
```

You can now run it from anywhere like this:

```bash
python -m wellness_hub.planner.run
```

---

## 🧪 Manual Test Discovery

To run all test files manually:

```bash
python -m unittest discover
```

---
