import openai
import os
import requests
import json

# Initialize the OpenAI API client
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to call OpenAI API for code review
def review_code(code):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Review the following code for best practices, potential bugs, and improvements:\n\n{code}",
        max_tokens=500
    )
    return response.choices[0].text.strip()

# Function to get the changed files from the pull request
def get_changed_files(pr_url, token):
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(pr_url, headers=headers)
    response.raise_for_status()
    pr_data = response.json()
    files_url = pr_data["url"] + "/files"
    response = requests.get(files_url, headers=headers)
    response.raise_for_status()
    files_data = response.json()
    return [file["filename"] for file in files_data]

# Function to add a comment to the pull request
def add_comment(pr_url, token, comment):
    comments_url = pr_url + "/comments"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "body": comment
    }
    response = requests.post(comments_url, headers=headers, data=json.dumps(data))
    response.raise_for_status()

# Main function
def main():
    pr_url = os.getenv("GITHUB_PULL_REQUEST_URL")
    token = os.getenv("GITHUB_TOKEN")
    changed_files = get_changed_files(pr_url, token)
    for file in changed_files:
        try:
            with open(file, 'rb') as f:
                code = f.read().decode('utf-8')
                review = review_code(code)
                add_comment(pr_url, token, f"Review for `{file}`:\n\n{review}")
        except UnicodeDecodeError:
            add_comment(pr_url, token, f"Review for `{file}`:\n\nUnable to decode file content. Skipping review.")

if __name__ == "__main__":
    main()
