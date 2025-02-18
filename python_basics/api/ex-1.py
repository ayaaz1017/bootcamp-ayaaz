import requests

def fetch_public_repositories():
    url = "https://api.github.com/repositories"
    response = requests.get(url)
    
    if response.status_code == 200:
        repositories = response.json()
        for repo in repositories[:10]:  # Fetching only first 10 repositories
            print(repo["name"])
    else:
        print(f"Failed to fetch repositories. Status code: {response.status_code}")

if __name__ == "__main__":
    fetch_public_repositories()
