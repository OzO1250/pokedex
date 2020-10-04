import requests
import argparse
import read_gsheet as gsheet
import compare_lists as cmp
from datetime import datetime

endpoint = "https://pokeapi.co/api/v2/pokemon"
poketest = []

def main():
    offset = input("Initial offset: ")
    api_call(offset)
    pokemon=cmp.compare_poke(poketest,gsheet.read_file())
    gsheet.write_file(pokemon)

def api_call(offset):
    parameters = {
        "limit": 20,
        "offset": offset
    }
    response = requests.get(endpoint, params = parameters)
    print(offset)
    #total_pokemon = response.json()['count']
    results = response.json()['results']
    if results:
        for d in results:
            poke_id = d['url'].split("/")
            timestamps = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            poketest.append([poke_id[6], d['name'], d['url'], timestamps])
        print(*poketest, sep='\n')

        next_page = input('Want to see more Pokémon?')
        if next_page == ('y'):
            api_call(offset=int(offset) + 20)
    else:
        print("No values")

# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Step 1. Input an integer to start loading Pokémon from the position in the Pokédex. \nStep 2. After the initial 20 Pokémon load type 'y' to keep loading new Pokémon or simply press Enter to finish.", formatter_class=argparse.RawTextHelpFormatter)
	args = parser.parse_args()
	main()