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
    # dont remove first num
    count1 = 0
    prev = report[0]
    for i in range(1, len(report)):
        if report[i] - prev > 3 or report[i] - prev <= 0:
            count1 += 1
        else:
            prev = report[i]
    
    #remove first num
    count2 = 0
    for i in range(2, len(report)):
        if report[i] - report[i-1] > 3 or report[i] - report[i-1] <= 0:
            count2 += 1
            break
    if count1 >= 2 and count2 == 1:
        return False 
    else:
        return True

def day2_helper_des(report):
    # dont remove first num
    count1 = 0
    prev = report[0]
    for i in range(1, len(report)):
        if report[i] - prev >= 0 or report[i] - prev < -3:
            count1 += 1
        else:
            prev = report[i]
    
    #remove first num
    count2 = 0
    for i in range(2, len(report)):
        if report[i] - report[i-1] >= 0 or report[i] - report[i-1] < -3:
            count2 += 1
            break
    if count1 >= 2 and count2 == 1:
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