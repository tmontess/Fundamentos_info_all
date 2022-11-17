import requests, os

url = "https://pokeapi.co/api/v2/pokemon/pikachu"
r=requests.get(url)

"""pokeapi.co es el dominio"""

print(r.headers)

utl_pokemon = "https://pokeapi.co/api/v2/pokemon"
r_pok = requests.get("https://pokeapi.co/api/v2/pokemon")
print(r_pok.json()["count"], "pokemons")

"https://pokeapi.co/api/v2/abilities"
"https://pokeapi.co/api/v2/abilities2" #segunda abilidad

# que me imprima todas la habilidades en un nuevo archivo
with open("ficha_tecnica_pokemon.txt", "a") as arch:
    arch.write( str(requests.get("https://pokeapi.co/api/v2/pokemon/pikachu").json()["abilities"]))
    arch.write("\n" + str(requests.get("https://pokeapi.co/api/v2/pokemon/sylveon").json()["abilities"]))
    
#ultimo punto no lo entendi 