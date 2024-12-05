'''
    UTILS:
    Given a list of numbers, return the middle number.
'''
def get_middle_number(number_list: list[int]) -> int:
    return number_list[len(number_list) // 2]


'''
    PART 1:
    Given a number, a list of next numbers and a list of rules, check if the number is in a valid position.
'''
def is_valid_position(number: int, next_numbers: list[int], number_rules: list[str]) -> bool:
    for rule in number_rules:
        if rule.split("|")[1] == number:
            if rule.split("|")[0] in next_numbers:
                return False
            
    return True


'''
    PART 2:
    Given a list of uncorrect updates, return the list of fixed updates.
'''
def fix_updates(bad_updates: list[str], rules: list[str]) -> list[str]:
    fixed_updates: list[str] = []
    for update in bad_updates:
        number_list: list[str] = update.split(",")
        i = 0
        while i < len(number_list):
            if not is_valid_position(number_list[i], number_list[i + 1:], rules):
                for rule in rules:
                    if rule.split("|")[1] == number_list[i] and rule.split("|")[0] in number_list[i + 1:]:
                        index = number_list.index(rule.split("|")[0])
                        number_list[i] = rule.split("|")[0]
                        number_list[index] = rule.split("|")[1]        
                i = max(0, i - 1)
            else :
                i += 1
        fixed_updates.append(",".join(number_list))

    return fixed_updates


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = file.read()
        rules = data.split("\n\n")[0].split("\n")
        updates = data.split("\n\n")[1].split("\n")

    correct_updates: list = []
    bad_updates: list = []

    for update in updates:
        number_list: list[str] = update.split(",")
        is_correct: bool = True
        for i in range(len(number_list)):
            if not is_valid_position(number_list[i], number_list[i + 1:], rules):
                is_correct = False
        if is_correct:
            correct_updates.append(update)
        else:
            bad_updates.append(update)

    correct_middle_numbers_sum: int = 0
    fixed_middle_numbers_sum: int = 0
    fixed_updates: list[str] = fix_updates(bad_updates, rules)

    for update in correct_updates:
        correct_middle_numbers_sum += get_middle_number(list(map(int, update.split(","))))

    for update in fixed_updates:
        fixed_middle_numbers_sum += get_middle_number(list(map(int, update.split(","))))
    
    print(correct_middle_numbers_sum)
    print(fixed_middle_numbers_sum)

    