# AI Dev Onboarding Assistant

A **Streamlit** web application frontend for interacting with the AI Dev Onboarding Assistant project, designed to
provide a clean interface and streamline common actions using a `Makefile`.

---

## 📦 Overview

This repository hosts the **Streamlit-based GUI** for AI Dev Onboarding Assistant. It uses a `Makefile` to simplify
environment setup, dependency management, and app execution.

---

## 🗂️ Project Structure

```
ai-dev-onboarding-assistant/
├── src/                   # Application source code
├── .gitignore
├── Makefile               # CLI automation commands
├── pyproject.toml         # Project metadata and dependencies
├── infra/                 # Terraform infrastructure code
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
   git clone https://github.com/sebastianhidalgoGL/ai-dev-onboarding-assistant
   cd ai-dev-onboarding-assistant
   ```

**Create an environment using venv**

In your terminal, type:

```bash
python -m venv .venv
```

A folder named ".venv" will appear in your project. This directory is where your virtual environment and its
dependencies are installed.

**Activate your environment**

In your terminal, activate your environment with one of the following commands, depending on your operating system.

```bash
# Windows command prompt
.venv\Scripts\activate.bat

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS and Linux
source .venv/bin/activate
```   

2. **Install dependencies using Make**
```bash
   make install
   ```

3. 🔑 Setting Up Secrets for Streamlit

   To securely use your OpenAI API key within the project, follow these steps:

    1. **Navigate to your project root (if not already there):**

   ```bash
   cd /ai-dev-onboarding-assistant
   ```

    2. **Create the `.env` directory:**

   ```bash
   touch .env
   ```

    3. Inside the `.env` file:**

   ```bash
   nano .env
   ```
   Note: Follow the `.env.example` file

    4. **Add your OpenAI API key and SQL DB: 

   ```bash
   OPENAI_API_KEY="your-openai-api-key-here"
   SQL_PASSWORD="you-sql-password"
   SQL_USER="you-sql-user"
   SQL_HOST="you-sql-host"
   SQL_DB="you-sql-db"
   ```

    5. **Save and close the file.**

   Your `.env` file is now configured, and Streamlit will be able to access the OpenAI API key and SQL DB securely.

5. **Start the Streamlit app**

   ```bash
   make start
   ```

   This will launch the app at [http://localhost:8501](http://localhost:8501)

---

## 🧪 Common Make Commands

| Command          | Description                             |
|------------------|-----------------------------------------|
| `make install`   | Installs Python dependencies            |
| `make run`       | Runs the Streamlit app (alias to start) |
| `make run start` | Starts the app via Streamlit            |

*Run `make` by itself to see all available commands.*

# Terraform Setup for Supabase and GitHub

This project uses Terraform to manage infrastructure for Supabase and GitHub. Follow the steps below to set up and start using Terraform.

## Prerequisites

1. Install [Terraform](https://developer.hashicorp.com/terraform/downloads).
2. Ensure you have a Supabase account and API key.
3. Ensure you have a GitHub account and a Personal Access Token (PAT) with repository permissions.

## Initial Setup

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd ai-dev-onboarding-assistant/infra
   ```

2. Create a `secrets.auto.tfvars` file (already included in `.gitignore`) with your credentials:
   - Supabase API URL, API Key, Organization ID, Region, and Database Password.
   - GitHub Token, Owner, and Repository Name.

   Example:
   ```hcl
   supabase_api_url      = "https://api.supabase.io"
   supabase_api_key      = "your-supabase-api-key"
   supabase_project_name = "your-project-name"
   supabase_org_id       = "your-org-id"
   supabase_region       = "your-region"
   supabase_db_password  = "your-secure-password"

   github_token          = "your-github-token"
   github_owner          = "your-github-username"
   github_repo_name      = "your-repo-name"
   ```

3. Initialize Terraform:
   ```bash
   terraform init
   ```

## Usage

1. Plan the infrastructure changes:
   ```bash
   terraform plan
   ```

2. Apply the changes to create resources:
   ```bash
   terraform apply
   ```

3. After applying, Terraform will output:
   - The Supabase project ID.
   - The GitHub repository URL.

## Notes

- The `secrets.auto.tfvars` file is ignored by Git to protect sensitive information.
- Make sure to keep your API keys and tokens secure.

## Cleanup

To destroy the created resources, run:
```bash
terraform destroy
```

## Additional Resources

- [Terraform Documentation](https://developer.hashicorp.com/terraform/docs)
- [Supabase Documentation](https://supabase.com/docs)
- [GitHub API Documentation](https://docs.github.com/en/rest)

### 🐳 Docker

You can run this application using Docker in two ways:

#### Using Dockerfile directly

1. **Build the Docker image:**

   ```bash
   docker build -t ai-dev-onboarding-assistant .
   ```

2. **Run the container:**

   ```bash
   docker run -p 8501:8501 --env-file .env ai-dev-onboarding-assistant
   ```

   This will start the application and make it available at [http://localhost:8501](http://localhost:8501)

#### Using Docker Compose

1. **Make sure you have a `.env` file with your environment variables:**

   Follow the instructions in the "Setting Up Secrets for Streamlit" section above to create your `.env` file.

2. **Build and start the services:**

   ```bash
   docker-compose build --no-cache && docker-compose up -d
   ```

   This will build the Docker image if needed and start the container. The application will be available at [http://localhost:8501](http://localhost:8501)

3. **To stop the services:**

   ```bash
   docker-compose down
   ```

**Note:** Both methods require you to have a properly configured `.env` file with your API keys and database credentials as described in the "Setting Up Secrets for Streamlit" section.