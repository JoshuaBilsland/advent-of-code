def extract_input(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            lines.append(line.strip())
    return lines


def main():
    # ***Problem 1 Solution***
    input_contents = extract_input("2024/day-05/input.txt")
    input_contents.pop(input_contents.index(""))
    page_rules = []
    page_updates = []
    for line in input_contents:
        if "|" in line:
            page_rules.append(line.split("|"))
        else:
            page_updates.append(line.split(","))


if __name__ == "__main__":
    main()
