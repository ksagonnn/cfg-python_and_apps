import requests
import random

# 1. Generate a random number between 1 and 151 to use as the Pokemon ID number

def get_random_pokemon_id():
    return random.randint(1, 151)

# 2. Using the Pokemon API get a Pokemon based on its ID number

def get_pokemon_by_id(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    return response.json()

# 3. Create a dictionary that contains the returned Pokemon's name, id, height and weight

def get_pokemon_data(pokemon_info):
    return {
        "name": pokemon_info["name"],
        "id": pokemon_info["id"],
        "height": pokemon_info["height"],
        "weight": pokemon_info["weight"],
    }

# 4. Get a random Pokemon for the player and another for their opponent

def get_random_pokemon():
    pokemon_id = get_random_pokemon_id()
    pokemon_info = get_pokemon_by_id(pokemon_id)
    return get_pokemon_data(pokemon_info)

player_pokemon = get_random_pokemon()
opponent_pokemon = get_random_pokemon()

# 5. Ask the user which stat they want to use (id, height or weight)

stat = input("Which stat would you like to use (id, height, or weight)? ")

# 6. Compare the player's and opponent's Pokemon on the chosen stat to decide who wins

if player_pokemon[stat] > opponent_pokemon[stat]:
    winner = "player"
else:
    winner = "opponent"

print(f"Player's Pokemon: {player_pokemon['name']} ({player_pokemon[stat]})")
print(f"Opponent's Pokemon: {opponent_pokemon['name']} ({opponent_pokemon[stat]})")
print(f"The winner is the {winner}!")

