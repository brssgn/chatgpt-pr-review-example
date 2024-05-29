import os
import requests
import json

# GitHub and OpenAI API credentials
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# GitHub API headers
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

def get_pull_request_changes(repo, pr_number):
    """Fetch pull request files and changes."""
    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}/files"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

import openai

def generate_review_text(changes):
    """Use OpenAI API to generate review comments based on code changes."""
    prompt = "Review the following code changes and provide feedback:\n\n"
    prompt += "\n\n".join([f"File: {file['filename']}\n```diff\n{file['patch']}\n```" for file in changes])
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a code reviewer."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

def post_comment_to_pr(repo, pr_number, comment):
    """Post a comment to a pull request."""
    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    payload = {"body": comment}
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

def main():
    repo = "username/repository"  # Specify your repository
    pr_number = 1  # Specify the pull request number

    # Get PR changes
    changes = get_pull_request_changes(repo, pr_number)

    # Generate review comment
    review_comment = generate_review_text(changes)

    # Post review comment to the PR
    post_comment_to_pr(repo, pr_number, review_comment)

if __name__ == "__main__":
    main()
