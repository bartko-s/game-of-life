# -*- coding: utf-8 -*-#
import time
import os
import random


class BaseApp():
    NUM_ROWS = 35
    NUM_COLS = 45

    SPEED = 0.25

    DEAD_CELL_SYMBOL = ' '
    LIVE_CELL_SYMBOL = '*'

    def build_random_grid(self, rows, cols):
        return [[random.choice([self.DEAD_CELL_SYMBOL, self.LIVE_CELL_SYMBOL])
                 for i in range(1, cols + 1)] for i in range(1, rows + 1)]

    def display_grid(self, grid_):
        for row in grid_:
            line = ''
            for cell in row:
                line += ' ' + cell
            print(line)

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def calculate_cell_state_for_next_round(self, current_cell, *args):
        num_lives = args.count(self.LIVE_CELL_SYMBOL)

        if current_cell == self.LIVE_CELL_SYMBOL:
            if 2 <= num_lives <= 3:
                return self.LIVE_CELL_SYMBOL
        else:
            if 3 == num_lives:
                return self.LIVE_CELL_SYMBOL

        return self.DEAD_CELL_SYMBOL

    def calculate(self, grid):
        num_rows = len(grid)
        num_cols = len(grid[0])

        result = [[] for i in range(1, num_rows + 1)]

        for row_index, row in enumerate(grid):
            for col_index, cell in enumerate(row):
                cells = []
                # top left cell
                if col_index > 0 and row_index > 0:
                    cells.append(grid[row_index - 1][col_index - 1])

                # top cell
                if row_index > 0:
                    cells.append(grid[row_index - 1][col_index])

                # top right cell
                if col_index < num_cols - 1 and row_index > 0:
                    cells.append(grid[row_index - 1][col_index + 1])

                # left cell
                if col_index > 0:
                    cells.append(grid[row_index][col_index - 1])

                # right cell
                if col_index < num_cols - 1:
                    cells.append(grid[row_index][col_index + 1])

                # bottom left cell
                if col_index > 0 and row_index < num_rows - 1:
                    cells.append(grid[row_index + 1][col_index - 1])

                # bottom cell
                if row_index < num_rows - 1:
                    cells.append(grid[row_index + 1][col_index])

                # bottom right cell
                if col_index < num_cols - 1 and row_index < num_rows - 1:
                    cells.append(grid[row_index + 1][col_index + 1])

                new_state = self.calculate_cell_state_for_next_round(cell, *cells)
                result[row_index].append(new_state)

        return result

    def run(self):
        grid = self.build_random_grid(self.NUM_ROWS, self.NUM_COLS)
        while True:
            self.clear_terminal()
            grid = self.calculate(grid)
            self.display_grid(grid)
            time.sleep(self.SPEED)