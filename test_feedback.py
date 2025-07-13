import requests

url = 'http://127.0.0.1:8000/submit-feedback/'

data = {
    "name": "Diya Gupta",
    "email": "diya@example.com",
    "message": "Testing feedback API!"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response Text:", response.text)  # Use .text instead of .json()