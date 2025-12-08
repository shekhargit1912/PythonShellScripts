import requests

urls=["http://localhost:9113/metrics","http://localhost:9114/metrics"]

for url in urls:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Service at {url} is UP")
        else:
            print(f"Service at {url} is DOWN. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Service at {url} is DOWN. Error: {str(e)}")

        
