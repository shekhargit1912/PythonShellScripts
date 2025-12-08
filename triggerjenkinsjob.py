import requests

from requests.auth import HTTPBasicAuth

jenkins_url = "http://jenkins.example.com/job/YourJobName/build"
username = "your_username"
password = "your_api_token_or_password"

response = requests.post(jenkins_url, auth=HTTPBasicAuth(username, password))
if response.status_code == 201:
    print("Jenkins job triggered successfully.")


#print build status

build_status_url = "http://jenkins.example.com/job/YourJobName/lastBuild/api/json"
status_response = requests.get(build_status_url, auth=HTTPBasicAuth(username, password))
print("Build Status:", status_response.json().get("result"))
