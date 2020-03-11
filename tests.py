'''
Contains the patterns that can be tested on the game.
If you want to add a pattern, add it in the same manner as other patterns are
and run the program to create a json file of patterns.
'''
import numpy as np
import json

# Gosper Glider Gun
pattern_1 = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Pulsar
pattern_2 = np.zeros(shape=(17, 17), dtype=int)
pattern_2[2, 4:7] = 1
pattern_2[4:7, 7] = 1
pattern_2 += pattern_2.T
pattern_2 += pattern_2[:, ::-1]
pattern_2 += pattern_2[::-1, :]

# Glider
pattern_3 = np.array([[1, 0, 0],
                     [0, 1, 1],
                     [1, 1, 0]])

# Spaceship
pattern_4 = np.array([[0, 0, 1, 1, 0],
                     [1, 1, 0, 1, 1],
                     [1, 1, 1, 1, 0],
                     [0, 1, 1, 0, 0]])

# Block Switch Engine
pattern_5 = np.array([[0, 0, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 0, 1, 0, 1, 1],
                     [0, 0, 0, 0, 1, 0, 1, 0],
                     [0, 0, 0, 0, 1, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0],
                     [1, 0, 1, 0, 0, 0, 0, 0]])

# Boat
pattern_6 = np.array([[1, 1, 0],
                     [1, 0, 1],
                     [0, 1, 0]])

# R Pentomino
pattern_7 = np.array([[0, 1, 1],
                     [1, 1, 0],
                     [0, 1, 0]])

# Beacon
pattern_8 = np.array([[0, 0, 1, 1],
                     [0, 0, 1, 1],
                     [1, 1, 0, 0],
                     [1, 1, 0, 0]])

# Acorn
pattern_9 = np.array([[0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0],
                     [1, 1, 0, 0, 1, 1, 1]])


# Creating a dictionary of lists to save the patterns
patterns = {'glider_gun': pattern_1.tolist(), 'pulsar': pattern_2.tolist(), 'glider': pattern_3.tolist(),
            'spaceship': pattern_4.tolist(), 'block_switch_engine': pattern_5.tolist(), 'boat': pattern_6.tolist(),
            'r_pentomino': pattern_7.tolist(), 'beacon': pattern_8.tolist(), 'acorn': pattern_9.tolist()}

# Saving to json file
with open('patterns.json', 'w') as pattern_file:
    json.dump(patterns, pattern_file)
