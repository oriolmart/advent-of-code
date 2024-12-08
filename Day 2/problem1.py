file = open("input.txt", "r")

total_safe: int = 0

for line in file:

    safe: bool = True
    increasing: bool = True
    report: list[int] = []


    for aux in line.split():
        report.append(int(aux))

    diff: int = report[0] - report[1]
    if diff > 0:
        increasing = False

    for level in range(len(report) - 1):
        diff = report[level] - report[level + 1]
        if diff == 0:
            safe = False
            break
        elif diff > 0 and increasing:
            safe = False
            break
        elif diff < 0 and not increasing:
            safe = False
            break

        if abs(diff) < 1 or abs(diff) > 3:
            safe = False
            break

    if safe:
        total_safe += 1

print(total_safe)
