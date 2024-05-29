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
def get_changed_files():
    pr_url = os.getenv("GITHUB_PULL_REQUEST_URL")
    response = requests.get(pr_url)
    pr_data = response.json()
    files_url = pr_data["url"] + "/files"
    response = requests.get(files_url)
    files_data = response.json()
    return [file["filename"] for file in files_data]

# Function to add a comment to the pull request
def add_comment(comment):
    pr_url = os.getenv("GITHUB_PULL_REQUEST_URL")
    comments_url = pr_url + "/comments"
    headers = {
        "Authorization": f"token {os.getenv('GITHUB_TOKEN')}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "body": comment
    }
    requests.post(comments_url, headers=headers, data=json.dumps(data))

# Main function
def main():
    changed_files = get_changed_files()
    for file in changed_files:
        with open(file, 'r') as f:
            code = f.read()
            review = review_code(code)
            add_comment(f"Review for `{file}`:\n\n{review}")

if __name__ == "__main__":
    main()
