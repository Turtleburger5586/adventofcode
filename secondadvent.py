def report_checker(reports: list[list[int]]) -> int:
    safe_reports: int = 0

    for report in reports:
        stupid: int = 0
        unsafe: bool = False
        decreasing: bool = False
        prev: int = 0
        for level in report:
            if stupid == 0:
                prev = level
                stupid+=1
            elif stupid == 1:
                if level > prev and (level-prev)<=3:
                    prev=level
                elif level < prev and (prev-level)<=3:
                    prev=level
                    decreasing = True
                else:
                    unsafe = True
                    break
                stupid+=1
            else:
                if decreasing==True:
                    if level < prev and (prev-level)<=3:
                        prev=level
                    else:
                        unsafe = True
                        break
                elif decreasing==False:
                    if level > prev and (level-prev)<=3:
                        prev=level
                    else:
                        unsafe = True
                        break
        if unsafe==False:
            safe_reports += 1

    return safe_reports

def updated_report_checker(reports: list[list[int]]) -> int:
    safe_reports: int = 0

    def checker(report: list[int]) -> bool:
        stupid: int = 0
        decreasing: bool = False
        prev: int = 0
        for level in report:
            if stupid == 0:
                prev = level
                stupid+=1
            elif stupid == 1:
                if level > prev and (level-prev)<=3:
                    prev=level
                elif level < prev and (prev-level)<=3:
                    prev=level
                    decreasing = True
                else:
                    return True
                stupid+=1
            else:
                if decreasing==True:
                    if level < prev and (prev-level)<=3:
                        prev=level
                    else:
                        return True
                elif decreasing==False:
                    if level > prev and (level-prev)<=3:
                        prev=level
                    else:
                        return True
        return False

    for report in reports:
        unsafe: bool = checker(report)
        if unsafe==True:
            i: int = 0
            while True:
                temp: list[int] = report.copy()
                temp.pop(i)
                print(temp)
                unsafe=checker(temp)
                i+=1
                if unsafe==False or i>=len(report):
                    break
        if unsafe==False:
            safe_reports += 1

    return safe_reports


reports: list[list[int]] = []

puzzle_input = open('problem2.txt', 'r')

for line in puzzle_input:
    report: list[int] = []
    levels = line.split()
    for level in levels:
        report.append(int(level))
    reports.append(report)


print(report_checker(reports))
print(updated_report_checker(reports))