def extract_input(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            lines.append(list(line.strip()))
    return lines


class Guard:
    def __init__(self, starting_row, starting_column):
        self.__row = starting_row
        self.__column = starting_column

        # Symbols
        self.__up_symbol = "^"
        self.__down_symbol = "v"
        self.__left_symbol = "<"
        self.__right_symbol = ">"

        # Movements
        self.__up_move = (-1, 0)
        self.__down_move = (1, 0)
        self.__left_move = (0, -1)
        self.__right_move = (0, 1)

        # Map symbol to movement
        self.__direction_map = {
            self.__up_symbol: self.__up_move,
            self.__down_symbol: self.__down_move,
            self.__left_symbol: self.__left_move,
            self.__right_symbol: self.__right_move
        }

        # Guard starts off looking up
        self.__current_direction = self.__up_symbol

    def get_row(self):
        return self.__row

    def get_column(self):
        return self.__column

    def get_current_direction(self):
        return self.__current_direction

    def set_row(self, new_row):
        self.__row = new_row

    def set_column(self, new_column):
        self.__column = new_column

    def turn(self):
        if self.__current_direction == self.__up_symbol:
            self.__current_direction = self.__right_symbol

        elif self.__current_direction == self.__right_symbol:
            self.__current_direction = self.__down_symbol

        elif self.__current_direction == self.__down_symbol:
            self.__current_direction = self.__left_symbol

        elif self.__current_direction == self.__left_symbol:
            self.__current_direction = self.__up_symbol

    def get_next_pos(self):
        """Get the row and column index of the next position on the map."""
        next_movement = self.__direction_map[self.__current_direction]
        next_row = self.__row + next_movement[0]
        next_column = self.__column + next_movement[1]
        return next_row, next_column


def get_guard_positions(patrol_map):
    empty_space = "."
    obstacle = "#"
    # Find where the guard starts
    for row_index, row in enumerate(patrol_map):
        for column_index, column in enumerate(row):
            if column != empty_space and column != obstacle:
                guard = Guard(row_index, column_index)

    # Work out patrol route
    guard_on_map = True
    while guard_on_map:
        next_pos = guard.get_next_pos()
        # Check next potential position is within the map
        if 0 <= next_pos[0] < len(patrol_map) and 0 <= next_pos[1] < len(patrol_map[0]):
            # Check for an obstacle
            if patrol_map[next_pos[0]][next_pos[1]] == obstacle:
                # There is one, change direction
                while patrol_map[next_pos[0]][next_pos[1]] == obstacle:
                    guard.turn()
                    next_pos = guard.get_next_pos()
            # No obstacle
            else:
                # Go forward and mark old location with "X"
                current_row = guard.get_row()
                current_column = guard.get_column()
                patrol_map[current_row][current_column] = "X"

                # Make the move
                patrol_map[next_pos[0]][next_pos[1]] = guard.get_current_direction()
                guard.set_row(next_pos[0])
                guard.set_column(next_pos[1])

        else:
            # End loop, guard has left the map
            current_row = guard.get_row()
            current_column = guard.get_column()
            patrol_map[current_row][current_column] = "X"
            guard_on_map = False

    # Count number of positions the guard has visited
    count = 0
    for row in patrol_map:
        for column in row:
            if column == "X":
                count += 1
    return count


def main():
    # ***Problem 1 Solution***
    patrol_map = extract_input("2024/day-06/input.txt")
    print("X:", get_guard_positions(patrol_map))


if __name__ == "__main__":
    main()
