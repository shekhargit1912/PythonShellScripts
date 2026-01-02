import requests


url= "www.google.com"

def test_api_endpoint(url,auth=None):
    try:
        response= requests.get(url,auth=auth)
        content_type= response.headers.get('Content-Type','').lower()
        if response.status_code== 200:
            if 'application/json' in content_type:
                data= response.json()
                print(f'API endpoint {{url}} returned JSON data:')

        else:
            print("site is not reachable ")

    except requests.exceptions.RequestException as e:
        print(f"Error accessing {{url}}: {{str(e)}}")
    except ValueError as ve:
        print(f"Error parsing JSON from {{url}}: {{str(ve)}}")

test_api_endpoint(url)
                
