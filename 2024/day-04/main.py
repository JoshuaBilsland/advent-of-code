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


def main():
    # ***Problem 1 Solution***
    word_search = extract_word_search("2024/day-04/input.txt")
    print(check_around(word_search))


if __name__ == "__main__":
    main()
