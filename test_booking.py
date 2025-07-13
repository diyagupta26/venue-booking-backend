import requests

url = 'http://127.0.0.1:8001/create-booking/'  # 👈 use the correct port (8000 or 8001)

data = {
    "venue_id": 1,  # 👈 yahi venue ID hai
    "booked_by": "Diya",
    "date": "2025-07-15"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.json())