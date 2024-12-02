def extract_reports(file_path):
    reports = []
    with open(file_path, "r") as file:
        for report in file.readlines():
            reports.append(report.strip().split())
    return reports


def main():
    # ***Puzzle 1 Solution***
    reports_list = extract_reports("2024/day-02/input.txt")
    safe_reports_num = 0
    for report in reports_list:
        report = list(map(int, report))
        # zip() is used to pair the each element with the one after it
        # each pair is then checked to see if it is asc/desc and if they differ by 1-3
        # all checks that these conditions are true for each pair
        if all((currentIndex < nextIndex) and (abs(currentIndex - nextIndex) >= 1 and abs(currentIndex - nextIndex) <= 3) for currentIndex, nextIndex in zip(report, report[1:])):
            safe_reports_num += 1
        elif all((currentIndex > nextIndex) and (abs(currentIndex - nextIndex) >= 1 and abs(currentIndex - nextIndex) <= 3) for currentIndex, nextIndex in zip(report, report[1:])):
            safe_reports_num += 1
    print(safe_reports_num)


if __name__ == "__main__":
    main()
