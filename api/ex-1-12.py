import requests

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/"

def fetch_pokemon(pokemon_name):
    response = requests.get(f"{POKEAPI_URL}{pokemon_name.lower()}")

    if response.status_code == 200:
        data = response.json()
        types = [t['type']['name'] for t in data['types']]
        
        print(f"🟢 Pokémon: {data['name'].capitalize()}")
        print(f"🔥 Type(s): {', '.join(types)}")
    else:
        print("❌ Error: Pokémon not found.")

# Example usage
pokemon_name = input("Enter a Pokémon name: ")
fetch_pokemon(pokemon_name)
