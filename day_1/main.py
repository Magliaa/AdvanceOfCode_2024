'''
    PART 1:
    Given the two ordered list of integers, 
    return the distances between the two lists.
'''
def get_distances(ordered_left_list: list, ordered_right_list: list) -> int:
    distance: int = 0
    for i in range(len(ordered_left_list)):
        distance += abs(ordered_left_list[i] - ordered_right_list[i])
    return distance


'''
    PART 2:
    Given the two ordered list of integers,
    return the similiarity between the two lists.
'''
def get_similiarity(ordered_left_list: list, ordered_right_list: list) -> int:
    similiarity: int = 0
    for i in range(len(ordered_left_list)):
        try:
            starting_index = ordered_right_list.index(ordered_left_list[i])
            last_index = starting_index
            while last_index < len(ordered_right_list) and ordered_right_list[last_index] == ordered_left_list[i]:
                last_index += 1
            similiarity += ordered_left_list[i] * (last_index - starting_index)
        except ValueError:
            pass
    return similiarity


if __name__ == "__main__":    
    with open("input.txt", "r") as file:
        left_list = []
        right_list = []
        for line in file:
            left, right = line.split()
            left_list.append(int(left))
            right_list.append(int(right))

    ordered_left_list = sorted(left_list)
    ordered_right_list = sorted(right_list)

    print(get_distances(ordered_left_list, ordered_right_list)) 
    print(get_similiarity(ordered_left_list, ordered_right_list))

