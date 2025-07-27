import requests

url = "http://127.0.0.1:8000/register/"
data = {
    "username": "diya123",
    "email": "diya@example.com",
    "password": "test1234"
}

response = requests.post(url, json=data)
print("Status Code:", response.status_code)
print("Response:", response.json())