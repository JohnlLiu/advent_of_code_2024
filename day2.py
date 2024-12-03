with open('day2.txt') as f: s = f.readlines()
reports = []

for line in s:
    reports.append([int(x) for x in line.split()])

def day2_part1(reports):
    res = 0
    for report in reports:
        # check increasing
        for i in range(len(report) - 1):
            if report[i + 1] - report[i] > 3 or report[i + 1] - report[i] <= 0:
                break
            if i == len(report) - 2:
                res += 1
        
        # check decreasing 
        for j in range(len(report) - 1):
            if report[j + 1] - report[j] < -3 or report[j + 1] - report[j] >= 0:
                break
            if j == len(report) - 2:
                res += 1
    
    return res


def day2_helper_asc(report):
    count = 0
    prev = report[0]
    for i in range(1, len(report)):
        if report[i] - prev > 3 or report[i] - prev <= 0:
            count += 1
        else:
            prev = report[i]
    
    if count >= 2:
        return False 
    else:
        return True

def day2_helper_des(report):
    count = 0
    prev = report[0]
    for i in range(1, len(report)):
        if report[i] - prev >= 0 or report[i] - prev < -3:
            count += 1
        else:
            prev = report[i]
    
    if count >= 2:
        return False 
    else:
        return True

def day2_part2(reports):
    res = 0
    for report in reports:
       if day2_helper_asc(report) or day2_helper_asc(report[::-1]) or day2_helper_des(report) or day2_helper_des(report[::-1]):
           res += 1
        
    return res

print(day2_part1(reports))
print(day2_part2(reports))