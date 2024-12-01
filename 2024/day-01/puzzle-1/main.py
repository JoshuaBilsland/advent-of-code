import merge_sort as ms


def get_lists(file_path):
    list_one = []
    list_two = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            list_one.append(line[:line.index("   ")])
            list_two.append(line[line.index("   ")+3:-1])
    return list_one, list_two


def main():
    list_one, list_two = get_lists("2024/day-01/puzzle-1/input.txt")
    print(list_one)
    print("##########################")
    print(list_two)


if __name__ == "__main__":
    main()
