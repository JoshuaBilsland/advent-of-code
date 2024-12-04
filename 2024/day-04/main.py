def extract_word_search(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            lines.append(list(line.strip()))
    return lines


def main():
    # ***Problem 1 Solution***
    word_search = extract_word_search("2024/day-04/input.txt")
    print(word_search)
    

if __name__ == "__main__":
    main()
