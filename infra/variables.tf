variable "supabase_api_url" {
  description = "Supabase API URL"
  type        = string
}

variable "supabase_access_token" {
  description = "Supabase JWT"
  type        = string
  sensitive   = true
}

variable "supabase_project_name" {
  description = "Name of the Supabase project"
  type        = string
}

variable "supabase_org_id" {
  description = "Supabase organization ID"
  type        = string
}

variable "supabase_region" {
  description = "Region for the Supabase project"
  type        = string
}

variable "supabase_db_password" {
  description = "Password for the Supabase database"
  type        = string
  sensitive   = true
}

variable "github_token" {
  description = "GitHub Personal Access Token"
  type        = string
  sensitive   = true
}

variable "github_owner" {
  description = "GitHub organization or user name"
  type        = string
}

variable "github_repo_name" {
  description = "Name of the GitHub repository"
  type        = string
}
