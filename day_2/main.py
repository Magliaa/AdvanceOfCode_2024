'''
    UTILS:
    Given a list, determine if it is increasing, decreasing or unsorted.
'''
def get_list_order(list: list):
    if (all(list[i] <= list[i + 1] for i in range(len(list) - 1))):
        return "increasing"
    elif (all(list[i] >= list[i + 1] for i in range(len(list) - 1))):
        return "decreasing"
    else:
        return "unsorted"


'''
    PART 1:
    Given a report, determine if it is safe or not.
    A report is considered safe if the difference between any two consecutive numbers is between 1 and 3
    and all numbers are in increasing order or descending order.
'''
def is_safe(report: list):
    if (get_list_order(report) == "unsorted"):
        return False

    for i in range(len(report) - 1):
        if (abs(report[i] - report[i + 1]) < 1 or abs(report[i] - report[i + 1]) > 3):
            return False
        
    return True


'''
    PART 2:
    Given an unsafe report, determine if it is fixable or not.
    A report is considered fixable if we can remove a number from the report and make it safe.
'''
def is_fixable(report: list):
    for i in range(len(report) - 1):
        if (abs(report[i] - report[i + 1]) < 1 or abs(report[i] - report[i + 1]) > 3 or get_list_order(report) == "unsorted"):
            first_new_report: list = report[:i] + report[i + 1:]
            second_new_report: list = report[:i + 1] + report[i + 2:]
            
            if is_safe(first_new_report) or is_safe(second_new_report):
                return True
    return False


if __name__ == "__main__":    
    with open("input.txt", "r") as file:
        report_list: list = []
        for line in file:
            array: list = list(map(int, line.split()))
            report_list.append(array)
    
    safe_report_count: int = 0
    for report in report_list:
        if is_safe(report):
            safe_report_count += 1
        elif is_fixable(report):
            safe_report_count += 1

    print(safe_report_count)
          