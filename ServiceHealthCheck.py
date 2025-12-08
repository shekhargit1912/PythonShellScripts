import requests


def check_health_of_services(service_url):

    response = requests.get(service_url)
    if response.status_code == 200:
        print(f"Service at {service_url} is UP")
    else:
        print(f"Service at {service_url} is DOWN. Status Code: {response.status_code}")
    return response.status_code

# Example usage
service_urls = [
    "http://your-eks-service-1/health",
    "http://your-eks-service-2/health"
]
for url in service_urls:
    check_health_of_services(url)
