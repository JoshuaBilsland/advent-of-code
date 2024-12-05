def extract_word_search(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            lines.append(list(line.strip()))
    return lines


def check_around(grid):
    """Check each direction of the discovered letter X to find any "XMAS"s."""
    target_word = "XMAS"
    target_found_count = 0

    directions = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1),    # Right
        (-1, -1),  # Up-left
        (-1, 1),   # Up-right
        (1, -1),   # Down-left
        (1, 1)     # Down-right
    ]

    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == target_word[0]:  # If "X" is found
                for row_increment, column_increment in directions:
                    is_match = True
                    for step in range(1, 4):
                        new_row = row + row_increment * step
                        new_column = column + column_increment * step

                        # Boundary check
                        if not ((new_row >= 0 and new_row < len(grid)) and (new_column >= 0 and new_column < len(grid[row]))):
                            is_match = False
                            break

                        # Match check
                        if grid[new_row][new_column] != target_word[step]:
                            is_match = False
                            break

                    if is_match:
                        target_found_count += 1

    return target_found_count


def part_two_check_around(grid):
    """Check each direction for "MAS"s in the shape of an "X"."""
    mas_cross_count = 0

    directions = [
        [-1, -1],  # Up-left
        [1, 1],     # Down-right

        [-1, 1],   # Up-right
        [1, -1],   # Down-left
    ]

    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == "A":
                is_match = True

                up_left = list((row + directions[0][0], column + directions[0][1]))
                down_right = list((row + directions[1][0], column + directions[1][1]))

                up_right = list((row + directions[2][0], column + directions[2][1]))
                down_left = list((row + directions[3][0], column + directions[3][1]))

                # Check one diagonal
                if (all(0 <= x < len(grid) for x in up_left) and all(0 <= x < len(grid) for x in down_right)):
                    if not (grid[up_left[0]][up_left[1]] == "M" and grid[down_right[0]][down_right[1]] == "S" or
                            grid[up_left[0]][up_left[1]] == "S" and grid[down_right[0]][down_right[1]] == "M"):
                        is_match = False
                else:  # Change from directions would mean index outside of the grid
                    is_match = False

                # Check the other diagonal
                if (all(0 <= x < len(grid) for x in up_right) and all(0 <= x < len(grid) for x in down_left)):
                    if not (grid[up_right[0]][up_right[1]] == "M" and grid[down_left[0]][down_left[1]] == "S" or
                            grid[up_right[0]][up_right[1]] == "S" and grid[down_left[0]][down_left[1]] == "M"):
                        is_match = False
                else:  # Change from directions would mean index outside of the grid
                    is_match = False

                if is_match:
                    mas_cross_count += 1

    return mas_cross_count


def main():
    # ***Problem 1 Solution***
    word_search = extract_word_search("2024/day-04/input.txt")
    print(check_around(word_search))

    # ***Problem 2 Solution***
    print(part_two_check_around(word_search))


if __name__ == "__main__":
    main()
