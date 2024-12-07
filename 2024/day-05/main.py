def extract_input(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            lines.append(line.strip())
    return lines


def check_updates(page_rules, page_updates):
    correct_total = 0
    incorrect_total = 0

    for update in page_updates:
        relevant_rules = []
        # Get each rule pair where both X and Y are in the update
        for rule in page_rules:
            if all([num in update for num in rule]):
                relevant_rules.append(rule)

        # Order the rules by the number of a certain X appears
        # (which num as X is most common e.i has the most rules)
        x_number = {}
        for rule in relevant_rules:
            if rule[0] not in x_number:
                x_number[rule[0]] = 1
            else:
                x_number[rule[0]] = x_number[rule[0]] + 1
        x_number_sorted = sorted(
            x_number.items(),
            key=lambda x: x[1],
            reverse=True
        )

        # Apply the rules
        ordered_update = []
        for rule in x_number_sorted:
            ordered_update.append(rule[0])
        ordered_update = ordered_update + [
            item for item in update if item not in ordered_update
        ]

        # Check if already in the right order
        if update == ordered_update:
            correct_total += int(update[len(update)//2])
        else:
            # Problem 2 Section - get total for incorrect updates
            incorrect_total += int(ordered_update[len(update)//2])

    return correct_total, incorrect_total


def main():
    # ***Problem 1 & 2 Solution***
    input_contents = extract_input("2024/day-05/input.txt")
    input_contents.pop(input_contents.index(""))
    page_rules = []
    page_updates = []
    for line in input_contents:
        if "|" in line:
            page_rules.append(line.split("|"))
        else:
            page_updates.append(line.split(","))
    print(check_updates(page_rules, page_updates)[0])
    print(check_updates(page_rules, page_updates)[1])


if __name__ == "__main__":
    main()
