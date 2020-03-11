# jde_tasks
This repository contains the solutions to challenge tasks given by JDE Robot for GSoC 2020. It's an implementation of the Game of Life. Description of this game can be found here https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life.

`life.py` --> Module which can be used to play the Game of Life.


`play_gol.py` --> Interactive application to play the game on terminal.


`tests.py` --> Contains the patterns that can be tested on the game. If you want to add a pattern, add it in the same manner as other patterns are and run the program to create a json file of patterns.


`config.json` --> The configuration file containing previously saved config which the user chose. The file name can be provided when playing the game using `play_gol.py` to save or to load the config file.


`patterns.json` --> Contains the patterns provided in `tests.py` in a portable json format.
