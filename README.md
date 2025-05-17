# AI Dev Onboarding Assistant

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

3. 🔑 Setting Up Secrets for Streamlit

   To securely use your OpenAI API key within the project, follow these steps:

      1. **Navigate to your project root (if not already there):**

   ```bash
   cd /path/to/your/project
   ```

      2. **Create the `.streamlit` directory:**

   ```bash
   mkdir -p .streamlit
   ```

      3. **Create the `secrets.toml` file inside the `.streamlit` folder:**

   ```bash
   nano .streamlit/secrets.toml
   ```

      4. **Add your OpenAI API key to the file in the following format:**

   ```toml
   # .streamlit/secrets.toml
   OPENAI_API_KEY = "your-openai-api-key-here"
   ```

   Replace `"your-openai-api-key-here"` with your actual API key.

      5. **Save and close the file.**  

   Your `secrets.toml` file is now configured, and Streamlit will be able to access the OpenAI API key securely.

5. **Start the Streamlit app**

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

