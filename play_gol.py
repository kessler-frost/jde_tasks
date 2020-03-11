'''
Interactive application to play the game on terminal.
'''
import numpy as np
from life import GOL, show_available_symbols, show_pattern
import json

# Loading the json file containing all the patterns.
with open('patterns.json', 'r') as pattern_file:
    patterns = json.load(pattern_file)

# Displaying all the patterns for the user to choose.
for pat in patterns.keys():
    print('\n\nPattern name: ', pat)
    show_pattern(np.array(patterns[pat]))

chosen_pattern = input("\n\nWhich pattern do you choose? Write the name: ")
pattern = np.array(patterns[chosen_pattern], dtype=int)

# Asking the user whether to create a new configuration or use an existing one
new_config = int(input("Press 1 to create a new configuration or 0 to use the config from json file. "))

if new_config:

    # Taking input of all the required variables
    output_board_size = input("Provide size of the output board (default is 50): ")

    start_offset = input("Provide the size of start offset from top left corner for showing the pattern (default is 2): ")

    show_available_symbols()
    symbol = input("Provide symbol to use for displaying live cells (default is 'c'): ")
    delay = input("Provide delay after every iteration in milliseconds (default is 1): ")

    if not output_board_size:
        output_board_size = 50
    if not start_offset:
        start_offset = 2
    if not symbol:
        symbol = 'c'
    if not delay:
        delay = 1

    # Saving configuration if asked to do so.
    to_save = input("Do you want to save this config? (y|n): ")
    if to_save == 'y':

        config_dict = {'output_board_size': int(output_board_size), 'start_offset': int(start_offset), 'symbol': symbol, 'delay': int(delay)}

        filename = input("Filename to save file with: ")
        with open(filename, 'w') as config_file:
            json.dump(config_dict, config_file)

    # The game play begins here.
    gol = GOL(output_board_size=int(output_board_size), start_offset=int(start_offset))
    gol.play(pattern, symbol=symbol, delay=int(delay))

else:

    # Loading the configuration json file.
    filename = input("Filename to load config from: ")
    with open(filename, 'r') as read_file:
        config = json.load(read_file)

    # The game play begins here from the loaded config.
    gol = GOL(output_board_size=int(config['output_board_size']), start_offset=int(config['start_offset']))
    gol.play(pattern, symbol=config['symbol'], delay=int(config['delay']))
