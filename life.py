'''
Module which can be used to play the Game of Life.
'''
import numpy as np
import platform
from os import system
from time import sleep


class GOL:
    def __init__(self, output_board_size=50, start_offset=2):
        '''
        output_board_size:
            This is to ensure that appropriate space is given to the grid pattern to expand.

        start_offset:
            This is to show the initial pattern on a grid by a certain offset from top left,
            e.g if a pattern is to be shown in the middle of the board a larger value of offset
            can be given like 20 or 30. Default value given is small so that the pattern starts
            on the top left side of the board.
        '''
        self.N = output_board_size
        self.start_offset = start_offset

    def get_symbol(self, sym='c'):
        '''
        Returns the unicode of the symbol which is to
        be used for displaying cells which are alive.
        More symbols can be added here if required.
        '''
        if sym == 'c':
            return '\u25cf'
        if sym == 'sq':
            return '\u25A0'
        if sym == 'lc':
            return '\u2B24'

    def clear(self):
        '''
        Clears the screen to allow for the next grid to show up.
        '''
        if platform.system() == 'Windows':
            system('cls')
        else:
            system('clear')

    def apply_pattern(self, grid, pattern):
        '''
        Applying given pattern to a grid filled with zeros.
        '''
        grid[self.start_offset:self.start_offset + pattern.shape[0], self.start_offset:self.start_offset + pattern.shape[1]] = pattern
        return grid

    def create_cell_block(self, grid, i, j):
        '''
        Creating a cell block which is a 3x3 matrix containing the cell
        in question and all its nearby neighbours. This is required to
        handle the cases where the cell in question is on the corner or on
        the edge of the board in which case it lacks certain neighbours.
        The missing neighbours are padded as 0s to maintain uniformity for
        any type of cell (on edge or not).
        '''
        cell_block = np.zeros(shape=(3, 3), dtype=int)

        p_range = [0, 3]
        q_range = [0, 3]

        # The code below handles the corner cell cases
        # without hindering the functioning of normal cell cases
        if i == 0:
            p_range[0] = 1
        elif i == (self.N - 1):
            p_range[1] = 2
        if j == 0:
            q_range[0] = 1
        elif j == (self.N - 1):
            q_range[1] = 2

        for p in range(p_range[0], p_range[1]):
            for q in range(q_range[0], q_range[1]):
                cell_block[p][q] = grid[i - 1 + p][j - 1 + q]

        return cell_block

    def update_cells(self, old_grid):
        '''
        Updating the cells according to the current grid
        and creating a new grid of those updated cells.
        '''
        new_grid = old_grid.copy()

        for i in range(self.N):
            for j in range(self.N):
                cell_status = old_grid[i][j]
                cell_block = self.create_cell_block(old_grid, i, j)

                # Updating the cells status according to its neighbours
                if cell_status == 0:
                    n_alive = np.count_nonzero(cell_block)
                    if n_alive == 3:
                        new_grid[i][j] = 1
                else:
                    n_alive = np.count_nonzero(cell_block) - 1
                    if (n_alive < 2) or (n_alive > 3):
                        new_grid[i][j] = 0

        return new_grid

    def show_grid(self, grid, sym='c', delay=1):
        '''
        To display the grid using a symbol for live cells
        and after a delay measured in milliseconds.
        '''
        grid = grid.astype(str)
        grid[grid == '0'] = ' '
        grid[grid == '1'] = self.get_symbol(sym)
        self.clear()
        print(grid)
        sleep(0.1 * delay)

    def play(self, pattern, symbol='c', delay=1):
        '''
        To play the game starting with an initial given pattern,
        a symbol to represent live cells and a delay for printing
        the board in a readable manner.
        '''
        grid = np.zeros(shape=(self.N, self.N), dtype=int)
        grid = self.apply_pattern(grid, pattern)
        with np.printoptions(threshold=np.inf, linewidth=np.inf):
            try:
                while True:
                    old_grid = grid
                    self.show_grid(grid, symbol, delay)
                    grid = self.update_cells(old_grid)
            except KeyboardInterrupt:
                exit


def show_available_symbols():
    '''
    To show all the available symbols which can be used for live cells.
    '''
    print('\u25cf', " --> input 'c' for Circle")
    print('\u25A0', " --> input 'sq' for Square")
    print('\u2B24', " --> input 'lc' for Large Circle\n")


def show_pattern(pattern):
    '''
    To show a pattern in a human readable format.
    '''
    with np.printoptions(threshold=np.inf, linewidth=np.inf):
        pattern = pattern.astype(str)
        pattern[pattern == '0'] = ' '
        pattern[pattern == '1'] = '\u25cf'
        print(pattern)
