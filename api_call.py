import requests

API_TOKEN = "changeme"
URL = "https://jsonplaceholder.typicode.com/posts"  # Public test API

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

data = {
    "title": "CTF Challenge",
    "body": "This is a test post for API interaction.",
    "userId": 1
}

response = requests.post(URL, json=data, headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.json())
