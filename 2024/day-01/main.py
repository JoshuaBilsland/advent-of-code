import merge_sort as ms


# sorts the lists into ascending order
def get_lists(file_path):
    list_one = []
    list_two = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            list_one.append(int(line[:line.index("   ")]))
            list_two.append(int(line[line.index("   ")+3:-1]))
    return list_one, list_two


def main():
    # ***Puzzle 1 Solution***
    list_one, list_two = get_lists("2024/day-01/input.txt")
    list_one = ms.merge_sort(list_one)
    list_two = ms.merge_sort(list_two)

    total = 0
    # go through each pair and return the difference without any sign
    for num_one, num_two in zip(list_one, list_two):
        total += abs(num_one - num_two)
    print(total)

    # ***Puzzle 2 Solution***
    similarity_score = 0
    for num_one in list_one:
        similarity_score += (num_one * list_two.count(num_one))
    print(similarity_score)


if __name__ == "__main__":
    main()
