import requests

token = 'e111d7746f6527e1f02f32d483fc7d88'

#response =  requests.post('https://api.pokemonbattle.me:9104/pokemons', json = {
 
    #"trainer_token": token,
    #"name": "generate",
   # "photo": "generate"

#}, headers={'Content-Type': 'application/json', 'trainer_token' : token})

#response_put =  requests.put('https://api.pokemonbattle.me:9104/pokemons', json = {
 
    #"pokemon_id": "27995",
    #"name": "New Name",
    #"photo": "https://dolnikov.ru/pokemons/albums/008.png"

#}, headers={'Content-Type': 'application/json', 'trainer_token' : token})

response_add =  requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball', json = {
    "trainer_token": token,
    "pokemon_id": "27995"

}, headers={'Content-Type': 'application/json', 'trainer_token' : token})

print(response_add.text)