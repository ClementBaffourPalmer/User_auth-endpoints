import requests

# Base URL for server
BASE_URL = "http://127.0.0.1:8000/api/accounts/"

# Test Sign-Up
def test_signup():
    signup_url = f"{BASE_URL}signup/"
    data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "password123"
    }
    response = requests.post(signup_url, json=data)
    print("Sign-Up Response:", response.status_code)
    try:
        print("Response JSON:", response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response is not valid JSON:", response.text)

# Test Login
def test_login():
    login_url = "http://127.0.0.1:8000/api/token/"
    data = {
        "username": "testuser",
        "password": "password123"
    }
    response = requests.post(login_url, json=data)
    print("Login Response:", response.status_code)
    try:
        json_data = response.json()
        print("Response JSON:", json_data)
        return json_data.get("access")
    except requests.exceptions.JSONDecodeError:
        print("Response is not valid JSON:", response.text)
        return None

# Test Get Profile
def test_get_profile(token):
    profile_url = f"{BASE_URL}profile/"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(profile_url, headers=headers)
    print("Get Profile Response:", response.status_code)
    try:
        print("Response JSON:", response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response is not valid JSON:", response.text)

# Test Update Profile
def test_update_profile(token):
    update_url = f"{BASE_URL}profile/"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    data = {
        "email": "updated@example.com"
    }
    response = requests.put(update_url, headers=headers, json=data)
    print("Update Profile Response:", response.status_code)
    try:
        print("Response JSON:", response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response is not valid JSON:", response.text)


if __name__ == "__main__":
    print("Testing API Endpoints...")
    test_signup()  # Sign-up a new user
    token = test_login()  # Login to get a token
    if token:
        test_get_profile(token)  # Get user profile
        test_update_profile(token)  # Update user profile
