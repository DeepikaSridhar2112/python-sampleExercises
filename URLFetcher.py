import requests 
import json
def fetchApi(api_url,request_body=None):
    response={}
    if(request_body is None):
        response = requests.get(api_url)
    else:
        response= requests.post(api_url,json = json.loads(request_body))
    status_code = response.status_code 
    response_body = {}
    try:
            response_body = response.json()
            print("Response JSON data:")
            print(response_body)
    except requests.exceptions.JSONDecodeError:
            print("Response content is not valid JSON.")        
    return status_code, response_body
api_key="f37fef98ab3eca5406aca1f2e9a08386"
fetchApi(f"https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={api_key}")
url = 'https://www.w3schools.com/python/demopage.php'
my_request = '{"myInput": "test"}'
fetchApi(url,my_request)
