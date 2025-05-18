# AI Dev Onboarding Assistant

A **Streamlit** web application frontend for interacting with the AI Dev Onboarding Assistant project, designed to provide a clean interface and streamline common actions using a `Makefile`.

---

## 📦 Overview

This repository hosts the **Streamlit-based GUI** for AI Dev Onboarding Assistant. It uses a `Makefile` to simplify environment setup, dependency management, and app execution.

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

---

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

