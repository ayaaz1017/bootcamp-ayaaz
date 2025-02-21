import requests

# GitHub API endpoint for public events
url = "https://api.github.com/events"

# Fetch the data from GitHub API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    events = response.json()

    # Print the summary of recent public events
    for event in events:
        actor = event.get("actor", {}).get("login", "Unknown")
        event_type = event.get("type", "Unknown")
        repo_name = event.get("repo", {}).get("name", "Unknown")
        created_at = event.get("created_at", "Unknown time")

        print(f"Event Type: {event_type}")
        print(f"Actor: {actor}")
        print(f"Repository: {repo_name}")
        print(f"Timestamp: {created_at}")
        print("-" * 50)
else:
    print(f"Failed to retrieve events. Status code: {response.status_code}")
