import requests
#
from pathlib import Path

def upload_artifacts(artifact_path,artifact_url,repo,artifact_user,artifact_password):
    file_path= Path(artifact_path)
    if not file_path.is_file():
        print(f"Artifact file '{artifact_path}' does not exist.")
        return
    if file_path.is_file():
        with open(file_path,"rb") as file:
            url=f"{artifact_url}/{repo}/{file_path.name}"
            response=requests.put(url,data=file,auth=(artifact_user,artifact_password))
            if response.status_code in [200,201]:
                print(f"Artifact '{file_path.name}' uploaded successfully to '{url}'.")
            else:
                print(f"Failed to upload artifact. Status Code: {response.status_code}, Response: {response.text}")
# Example usage
artifact_path="C:/path/to/your/artifact.jar"
artifact_url="http://artifact-repo.example.com/repository"
repo="my-repo"
artifact_user="username"
artifact_password="password"
upload_artifacts(artifact_path,artifact_url,repo,artifact_user,artifact_password)
