# Pokedex

### Installation & Run intructions

**Step 1:** Install the Google Client Library and the Request library
Run the following commands to install the required libraries using pip:

`pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`

`pip install requests`

**Step 2:** Run the pokedex.py script.

`python pokedex.py`

***Note:*** You can add the -h argument to get help on how to use the script first

`python pokedex.py -h`

**Step 3:** Pokémon are sorted by number, and organized by pages with 20 records each, please select an initial Offset to start loading Pokémon, that is, select from which number you want to start seeing results.

**Step 4:** After the initial 20 records are shown on screen you will be asked if you want to keep loading results.

Type **"y"** and press ENTER if you wanto load 20 more Pokémon OR just press Enter to finish.

**Step 5:** Finally, open the Spreadsheet: https://docs.google.com/spreadsheets/d/1DQVQnKuKEL6gwLF9q4cnzKSUrNP23w52J-BOAe0ZRZE/edit?usp=sharing to check your results.

Previous results saved in the file will be merged with the new records obtained from the Pokémon API.
