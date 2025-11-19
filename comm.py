def find_common_elements(list1, list2):
    set2 = set(list2)
    result = []

    for x in list1:
        if x in set2 and x not in result:

            result.append(x)   # ensures duplicates appear only once

    return result


# Example
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

print(find_common_elements(list1, list2))   # Output → [3, 4]
