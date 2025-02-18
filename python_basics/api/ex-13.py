import requests

GITHUB_API_URL = "https://api.github.com/users/{}/events/public"

def fetch_github_contributions(username):
    response = requests.get(GITHUB_API_URL.format(username))

    if response.status_code == 200:
        events = response.json()
        commit_events = sum(1 for event in events if event["type"] == "PushEvent")

        print(f"🖥️ GitHub User: {username}")
        print(f"📌 Contributions in Public Repos: {commit_events} commits")
    else:
        print("❌ Error fetching GitHub contributions.")

# Example usage
github_user = input("Enter GitHub username: ")
fetch_github_contributions(github_user)
