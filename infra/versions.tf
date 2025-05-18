terraform {
  required_version = ">= 1.5.0"

  required_providers {
    supabase = {
      source  = "supabase/supabase"
      version = "~> 1.0"
    }
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}
provider "supabase" {
  access_token = var.supabase_access_token
}

provider "github" {
  token = var.github_token
  owner = var.github_owner
}