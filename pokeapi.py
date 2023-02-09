import requests
import csv

# endpoint com a lista dos pokemons
url = "https://pokeapi.co/api/v2/pokemon?limit=1000"

# Função pra obter os dados sobre os pokemons
def get_pokemon_info(name):
  # Request para pegar os dados sobre os pokemons
  response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
  
  # check statuscode 200
  if response.status_code == 200:
    pokemon_data = response.json()
    pokemon_abilities = pokemon_data['abilities']
    pokemon_types = pokemon_data['types']

    # Obtem o nome da habilidade
    pokemon_ability = pokemon_abilities[0]['ability']['name']

    # Obtem o tipo de pokemon
    pokemon_type = pokemon_types[0]['type']['name']

    return (pokemon_data['name'], pokemon_ability, pokemon_type)
  else:
    return None

# Request para obter a lista com todos os pokemons
response = requests.get(url)

# Check statuscode
if response.status_code == 200:

  # GET para obter a lista com todos os pokemons
  pokemons_data = response.json()['results']
  pokemons = [pokemon['name'] for pokemon in pokemons_data]
  
  # Valida se o nome do pokemon foi informado
  pokemon_name = input("Informe o nome do Pokemon (ou deixe em branco para obter uma lista com 10 Pokemons): ")
  if pokemon_name:
    # Obtem os dados sobre os pokemons
    pokemon_info = get_pokemon_info(pokemon_name)

    # Valida se o pokemon informado é valido
    if pokemon_info:
      # Escreve os dados sobre o pokemon no arquivo csv pokemon_info.csv
      with open('pokemon_info.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Ability", "Type"])
        writer.writerow(pokemon_info)
      print(f"Dados sobre o Pokemon {pokemon_name} foi salvo no arquivo pokemon_info.csv")
    else:
      print(f"Pokemon {pokemon_name} não foi encontrado")
  else:
    pokemons_info = []
    for pokemon in pokemons[:10]:
      pokemon_info = get_pokemon_info(pokemon)
      pokemons_info.append(pokemon_info)

    # Ordena os pokemons por habilidade
    pokemons_info.sort(key=lambda x: x[1])

    # Escreve os dados sobre os pokemons no arquivo csv pokemons_info.csv
    with open('pokemons_info.csv', 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(["Name", "Ability", "Type"])
      writer.writerows(pokemons_info)
    print(f"Dados sobre os 10 primeiros Pokemons na lista foi salvo no arquivo pokemons_info.csv")
else:
  print("Erro ao obter a lista de Pokemons")
