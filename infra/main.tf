resource "supabase_project" "project" {
  name              = var.supabase_project_name
  organization_id   = var.supabase_org_id
  region            = var.supabase_region
  database_password = var.supabase_db_password
}

resource "github_repository" "repo" {
  name        = var.github_repo_name
  description = "Repository for LlamaIndex and Streamlit integration"
  visibility  = "private"
}