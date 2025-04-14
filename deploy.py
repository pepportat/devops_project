import os
import sys
import requests

username = os.environ.get("PA_USERNAME")
token = os.environ.get("PA_API_TOKEN")
repo = os.environ.get("REPO_NAME").split('/')[1]

if not username or not token:
    print("Missing PythonAnywhere credentials.")
    sys.exit(1)

headers = {"Authorization": f"Token {token}"}
api_base = f"https://www.pythonanywhere.com/api/v0/user/{username}"

# Reload the web app
print("Reloading web app...")
response = requests.post(f"{api_base}/webapps/{username}.pythonanywhere.com/reload/", headers=headers)

if response.status_code == 200:
    print("Successfully reloaded!")
else:
    print(f"Failure: {response.status_code}, {response.text}")
