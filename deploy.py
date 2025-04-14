import os
import sys
import requests

username = os.environ.get("PA_USERNAME")
token = os.environ.get("PA_API_TOKEN")
repo = os.environ.get("REPO_NAME").split('/')[1]
branch = os.environ.get('BRANCH_NAME')

if not username or not token:
    print("Missing PythonAnywhere credentials.")
    sys.exit(1)

headers = {"Authorization": f"Token {token}"}
api_base = f"https://www.pythonanywhere.com/api/v0/user/{username}"

# Update files via git pull
print("Pulling latest code from repository...")
console_url = f"{api_base}/consoles/39294302/send_input/"
# Command to change to project directory and pull latest code
git_pull_command = (
    f"git pull && "
    f"git checkout {branch} && "
    f"cd ~/{repo} && "
    f"pip install -r requirements.txt"
    "\n"
)
# Send command to console
response = requests.post(
console_url,
headers=headers,
json={"input": git_pull_command}
)
if response.status_code != 200:
    print(f"Failed to execute git pull: {response.text}")

# Reload the web app
print("Reloading web app...")
response = requests.post(f"{api_base}/webapps/{username}.pythonanywhere.com/reload/", headers=headers)

if response.status_code == 200:
    print("Successfully reloaded!")
else:
    print(f"Failure: {response.status_code}, {response.text}")
