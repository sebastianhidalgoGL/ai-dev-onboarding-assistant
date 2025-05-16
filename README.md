# 🍌 Banana Bot Streamlit

A **Streamlit** web application frontend for interacting with the Banana Bot project, designed to provide a clean interface and streamline common actions using a `Makefile`.

---

## 📦 Overview

This repository hosts the **Streamlit-based GUI** for Banana Bot. It uses a `Makefile` to simplify environment setup, dependency management, and app execution.

---

## 🗂️ Project Structure

```
banana-bot-streamlit/
├── src/                   # Application source code          # Main Streamlit app
├── .gitignore
├── Makefile               # CLI automation commands
├── pyproject.toml         # Project metadata and dependencies
└── README.md
```

---

## 🛠️ Setup & Installation

### 🧰 Requirements

- Python 3.8+
- `make` (standard on macOS/Linux, installable on Windows via WSL or GNU Make)
- `pip` (Python package installer)

---

### 🚀 Quick Start

1. **Clone the repository**

   ```bash
   git clone https://github.com/sebastianhidalgoGL/banana-bot-streamlit.git
   cd banana-bot-streamlit
   ```

2. **Install dependencies using Make**

   ```bash
   make install
   ```

3. **Start the Streamlit app**

   ```bash
   make start
   ```

   This will launch the app at [http://localhost:8501](http://localhost:8501)

---

## 🧪 Common Make Commands

| Command        | Description                                 |
|----------------|---------------------------------------------|
| `make install` | Installs Python dependencies                |
| `make run`     | Runs the Streamlit app (alias to start)     |
| `make run start`   | Starts the app via Streamlit                |

*Run `make` by itself to see all available commands.*

