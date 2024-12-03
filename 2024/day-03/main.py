import re


def extract_memory(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            lines.append(line.strip())
    for line in lines:
        print(line)
        print("******************************")
    return lines


def main():
    memory_lines = extract_memory("2024/day-03/input.txt")


if __name__ == "__main__":
    main()
