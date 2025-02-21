import requests
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# AniList GraphQL API Endpoint
ANILIST_API_URL = "https://graphql.anilist.co"

# GraphQL Query for Anime details
query = gql("""
query ($title: String) {
  Media(search: $title, type: ANIME) {
    title {
      romaji
      english
    }
    description
    status
  }
}
""")

def fetch_anime_details(title):
    transport = RequestsHTTPTransport(url=ANILIST_API_URL)
    client = Client(transport=transport, fetch_schema_from_transport=True)

    variables = {"title": title}
    response = client.execute(query, variable_values=variables)

    anime = response.get("Media", {})
    print(f"🎥 Title: {anime['title']['english'] or anime['title']['romaji']}")
    print(f"📖 Description: {anime['description'][:200]}...")  # Show first 200 characters
    print(f"📺 Airing Status: {anime['status']}")

# Example usage
anime_title = input("Enter an anime title: ")
fetch_anime_details(anime_title)
