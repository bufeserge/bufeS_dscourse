# L01T14 : Data Structures - 2D Lists


# INSTRUCTIONS : Write a Python function that takes a grid made of # (mines) and - (safe spots)
#                Replace each - with a number showing how many mines are directly next to it (including diagonals)
#                Keep the # symbols as they are
#                Check all 8 directions around each -, but don’t go outside the grid.
#                Return a new grid with numbers instead of -, showing how many nearby mines each spot has.


# i’ll write a function called is_valid_position(grid, row, col) that checks if a given row and column are inside the grid boundaries, helping me avoid index errors when checking around each cell
# i’ll create the main function called minesweeper(grid). This will take the original grid as input and build a new version of it with numbers replacing the - characters:
#   -   loop through each cell in the grid using nested for loops (one for the row index and one for the column index).
#   -   if cell contains a #, i’ll copy it over to the new grid
#   -   if cell is a -, I’ll check all 8 adjacent positions, using is_valid_position to determine if im still in the grid. If the neighbouring cell calculated is # then inc counter
#   -   once all surrounding mines counted, ill replace that - with the number of mines, and add it to a new row list. Once row full ill append this row to the resulting grid
#   -   when whole grid is processed, i’ll return the new result grid

# POSITION VALID FUNCTION
def is_valid_position(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(
        grid[0]
    )  # Makes sure row and column are within limits


# MAIN NEW GRID FUNCTION
def minesweeper(grid):
    result = []  # This will hold the final grid with numbers and mines

    # Loop through each row by index
    for row_index in range(len(grid)):
        new_row = []  # Temp row to build updated line

        # Loop through each column in the row
        for col_index in range(len(grid[0])):
            cell = grid[row_index][col_index]  # Grab the current cell

            if cell == "#":
                new_row.append("#")  # If it's a mine, leave it as-is
            else:
                mine_count = 0  # Start counter for adjacent mines

                # List of directions to check: N, NE, E, SE, S, SW, W, NW
                directions = [
                    (-1, 0),
                    (-1, 1),
                    (0, 1),
                    (1, 1),
                    (1, 0),
                    (1, -1),
                    (0, -1),
                    (-1, -1),
                ]

                # Loop through all 8 directions
                for dr, dc in directions:
                    r, c = row_index + dr, col_index + dc
                    # Check if the position is in bounds and if it's a mine
                    if is_valid_position(grid, r, c) and grid[r][c] == "#":
                        mine_count += 1

                new_row.append(str(mine_count))  # Replace '-' with the mine count

        result.append(new_row)  # Add the fully processed row to result

    return result


# EXAMPLE GRID
test_grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
]

# RUN MAIN NEW GRID FUNCTION
output = minesweeper(test_grid)

# Display the output in a readable format
for row in output:
    print(" ".join(row))
