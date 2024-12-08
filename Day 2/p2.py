file = open("input.txt", "r")

total_safe: int = 0

for line in file:

    there_is_a_safe_report: bool = False
    report: list[int] = []

    for aux in line.split():
        report.append(int(aux))

    i: int = -1
    while i < len(report):
        increasing: bool = True
        safe: bool = True
        modified_report: list[int] = report.copy()
        if i != -1: modified_report.pop(i)

        diff: int = modified_report[0] - modified_report[1]
        if diff > 0:
            increasing = False

        for level in range(len(modified_report) - 1):
            diff = modified_report[level] - modified_report[level + 1]
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
            there_is_a_safe_report = True
            break
        i += 1

    if there_is_a_safe_report:
        total_safe += 1
    
print(total_safe)
