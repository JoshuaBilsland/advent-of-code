def extract_reports(file_path):
    reports = []
    with open(file_path, "r") as file:
        for report in file.readlines():
            reports.append(report.strip().split())
    return reports


def main():
    reports_list = extract_reports("2024/day-02/input.txt")


if __name__ == "__main__":
    main()
