import requests

# Sign-Up
signup_url = "http://127.0.0.1:8000/api/accounts/signup/"
signup_data = {
    "username": "testuser",
    "email": "test@example.com",
    "password": "password123"
}
response = requests.post(signup_url, json=signup_data)
print("Sign-Up Response:", response.json())

# Login
login_url = "http://127.0.0.1:8000/api/token/"
login_data = {
    "username": "testuser",
    "password": "password123"
}
response = requests.post(login_url, json=login_data)
tokens = response.json()
print("Login Response:", tokens)

# Access Profile
profile_url = "http://127.0.0.1:8000/api/accounts/profile/"
headers = {
    "Authorization": f"Bearer {tokens['access']}"
}
response = requests.get(profile_url, headers=headers)
print("Profile Response:", response.json())
