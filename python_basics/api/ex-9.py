import requests

# API URL for Rick and Morty characters
API_URL = "https://rickandmortyapi.com/api/character"

def fetch_characters():
    try:
        # Fetch data from the API
        response = requests.get(API_URL)
        
        if response.status_code == 200:
            data = response.json()
            characters = data.get("results", [])

            print("🛸 Rick and Morty Characters 🛸\n")
            for char in characters[:10]:  # Fetch first 10 characters
                name = char.get("name", "Unknown")
                species = char.get("species", "Unknown")
                status = char.get("status", "Unknown")
                
                print(f"👽 Name: {name}")
                print(f"🔬 Species: {species}")
                print(f"💀 Status: {status}")
                print("-" * 40)
        else:
            print(f"❌ Error: Failed to fetch data. Status code: {response.status_code}")

    except Exception as e:
        print(f"❌ Error: {e}")

# Run the function
fetch_characters()
