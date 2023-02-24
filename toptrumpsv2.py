import requests
import random

def get_random_pokemon_id():
    return random.randint(1, 151)

def get_pokemon_by_id(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    return response.json()

def get_pokemon_data(pokemon_info):
    return {
        "name": pokemon_info["name"],
        "id": pokemon_info["id"],
        "height": pokemon_info["height"],
        "weight": pokemon_info["weight"],
    }

def get_random_pokemon():
    pokemon_id = get_random_pokemon_id()
    pokemon_info = get_pokemon_by_id(pokemon_id)
    return get_pokemon_data(pokemon_info)

def display_pokemon(pokemon):
    print(f"Name: {pokemon['name']}")
    print(f"ID: {pokemon['id']}")
    print(f"Height: {pokemon['height']}")
    print(f"Weight: {pokemon['weight']}")

def choose_pokemon(player_pokemon_list):
    for i, pokemon in enumerate(player_pokemon_list):
        print(f"{i + 1}. {pokemon['name']}")
    choice = int(input("Choose a Pokemon (1, 2, 3, etc): ")) - 1
    return player_pokemon_list[choice]

def compare_pokemon(player_pokemon, opponent_pokemon, stat):
    if player_pokemon[stat] > opponent_pokemon[stat]:
        winner = "Player"
    else:
        winner = "Opponent"
    return winner

player_pokemon_list = [get_random_pokemon() for i in range(3)]
for pokemon in player_pokemon_list:
    display_pokemon(pokemon)

player_pokemon = choose_pokemon(player_pokemon_list)
opponent_pokemon = get_random_pokemon()

stat = input("Which stat would you like to use (id, height, or weight)? ")
winner = compare_pokemon(player_pokemon, opponent_pokemon, stat)
print(f"Player's Pokemon: {player_pokemon['name']} ({player_pokemon[stat]})")
print(f"Opponent's Pokemon: {opponent_pokemon['name']} ({opponent_pokemon[stat]})")
print(f"The winner is the {winner}!")
