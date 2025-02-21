import requests
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# Replace with your GitHub personal access token
GITHUB_TOKEN = "your_github_token_here"

# GraphQL API Endpoint
GITHUB_API_URL = "https://api.github.com/graphql"

# GraphQL Query to fetch repositories
query = gql("""
{
  viewer {
    login
    repositories(first: 10) {
      nodes {
        name
        description
      }
    }
  }
}
""")

# Set up GraphQL client
transport = RequestsHTTPTransport(
    url=GITHUB_API_URL,
    headers={"Authorization": f"Bearer {GITHUB_TOKEN}"}
)

client = Client(transport=transport, fetch_schema_from_transport=True)

# Execute the query
try:
    response = client.execute(query)

    # Extract repository data
    user = response["viewer"]["login"]
    repositories = response["viewer"]["repositories"]["nodes"]

    print(f"Repositories of GitHub User: {user}\n")
    for repo in repositories:
        print(f"Name: {repo['name']}")
        print(f"Description: {repo['description'] or 'No description available'}")
        print("-" * 40)

except Exception as e:
    print(f"Error: {e}")
