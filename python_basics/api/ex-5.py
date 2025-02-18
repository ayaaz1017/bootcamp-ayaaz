import requests
from requests_oauthlib import OAuth2Session
import os

# Bluesky API credentials (fill with your actual credentials)
client_id = "your_client_id"  # Your Bluesky client ID
client_secret = "your_client_secret"  # Your Bluesky client secret
redirect_uri = "your_redirect_uri"  # Your OAuth2 redirect URI

# Get your access token
authorization_url = "https://api.bsky.app/oauth/authorize"  # Bluesky OAuth URL
token_url = "https://api.bsky.app/oauth/token"  # Bluesky Token URL

# Assuming you already have the authorization code from OAuth2 flow
authorization_code = "authorization_code_here"  # Replace with actual code

# Create an OAuth2 session
oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)
token = oauth.fetch_token(token_url, client_secret=client_secret, authorization_response=authorization_code)

# Define the Bluesky API endpoint for posting a message
post_url = "https://api.bsky.app/v1/tweet"  # This is an example URL. Replace with actual Bluesky API endpoint.

# The message you want to post
message = "This is my first tweet using the Bluesky API! #BlueskyAPI"

# Set up the headers with the access token
headers = {
    "Authorization": f"Bearer {token['access_token']}",
    "Content-Type": "application/json",
}

# Prepare the payload to send the tweet
payload = {
    "status": message
}

# Post the message
response = requests.post(post_url, headers=headers, json=payload)

# Check if the message was successfully posted
if response.status_code == 201:
    print("Tweet posted successfully!")
else:
    print(f"Failed to post tweet. Status code: {response.status_code}")
    print(response.json())
