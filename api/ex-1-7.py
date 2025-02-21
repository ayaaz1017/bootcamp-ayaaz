import requests
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# SpaceX GraphQL API Endpoint
SPACEX_API_URL = "https://api.spacex.land/graphql/"

# GraphQL Query to fetch the latest launch details
query = gql("""
{
  launchLatest {
    mission_name
    launch_date_utc
    rocket {
      rocket_name
    }
    launch_site {
      site_name_long
    }
    links {
      video_link
    }
  }
}
""")

# Set up GraphQL client
transport = RequestsHTTPTransport(url=SPACEX_API_URL)
client = Client(transport=transport, fetch_schema_from_transport=True)

# Execute the query
try:
    response = client.execute(query)

    # Extract launch details
    launch = response["launchLatest"]
    mission_name = launch["mission_name"]
    launch_date = launch["launch_date_utc"]
    rocket_name = launch["rocket"]["rocket_name"]
    launch_site = launch["launch_site"]["site_name_long"]
    video_link = launch["links"]["video_link"]

    # Print the launch details
    print(f"🚀 Latest SpaceX Launch Details 🚀\n")
    print(f"Mission Name: {mission_name}")
    print(f"Launch Date (UTC): {launch_date}")
    print(f"Rocket: {rocket_name}")
    print(f"Launch Site: {launch_site}")
    print(f"Watch Video: {video_link if video_link else 'No video available'}")

except Exception as e:
    print(f"Error: {e}")
