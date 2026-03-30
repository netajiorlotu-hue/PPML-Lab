
def find_min_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    rest_min = find_min_recursive(lst[1:])
    return lst[0] if lst[0] < rest_min else rest_min

numbers = [5, 2, 9, 1, 7]
print(find_min_recursive(numbers))