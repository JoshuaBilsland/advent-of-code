import re


def extract_memory(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            lines.append(line.strip())
    return lines


def main():
    # ***Puzzle 1 Solution***
    memory_lines = extract_memory("2024/day-03/input.txt")
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    total = 0
    for line in memory_lines:
        # create list of mul(x,y) from the "memory"
        matches = re.findall(pattern, line)
        # Go through each list of mul(x,y) and calculate the result
        for match in matches:
            nums = list(map(int, re.findall(r"\d+", match)))
            total += nums[0] * nums[1]
    print(total)

    # ***Puzzle 2 Solution***
    memory_lines = extract_memory("2024/day-03/input.txt")
    pattern = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"
    total = 0
    instructions_enable = True
    for line in memory_lines:
        # create list of mul(x,y) from the "memory"
        matches = re.findall(pattern, line)
        # Go through each match, checking for do, don't and mul()
        for match in matches:
            if match == "do()":
                instructions_enable = True
            elif match == "don't()":
                instructions_enable = False
            else:
                if instructions_enable:
                    nums = list(map(int, re.findall(r"\d+", match)))
                    total += nums[0] * nums[1]
    print(total)


if __name__ == "__main__":
    main()
