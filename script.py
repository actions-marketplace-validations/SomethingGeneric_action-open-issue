from github import Github
import sys

# Replace with your GitHub username, repository name, and personal access token
username = sys.argv[1]
repository_name = sys.argv[2]
personal_access_token = sys.argv[3]

# Initialize the GitHub instance with your personal access token
g = Github(personal_access_token)

# Get the repository
repo = g.get_user(username).get_repo(repository_name)

# Create a new issue
issue_title = sys.argv[4]
issue_body = sys.argv[5]
issue = repo.create_issue(title=issue_title, body=issue_body)

print(f"Created issue: {issue.title}")
