output "supabase_project_id" {
  description = "The ID of the created Supabase project"
  value       = supabase_project.project.id
}

output "github_repo_url" {
  description = "The URL of the created GitHub repository"
  value       = github_repository.repo.html_url
}
