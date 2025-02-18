import requests
import sys

def fetch_user_details(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        user_data = response.json()
        print(f"Name: {user_data.get('name', 'N/A')}")
        print(f"Public Repos: {user_data.get('public_repos', 'N/A')}")
    else:
        print(f"Failed to fetch user details. Status code: {response.status_code}")

def main():
    if len(sys.argv) > 1:
        fetch_user_details(sys.argv[1])
    else:
        print("Usage: python script.py <github_username>")

if __name__ == "__main__":
    main()
