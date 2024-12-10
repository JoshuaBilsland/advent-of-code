def extract_input(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            lines.append(list(line.strip()))
    return lines


def main():
    # ***Problem 1 Solution***
    patrol_map = extract_input("2024/day-06/input.txt")


if __name__ == "__main__":
    main()
