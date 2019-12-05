number_list = [0, 1, 2, 3, 5, 5, 6, 7]

def linear_search(value, iterable):
    for index, val in enumerate(iterable):
        if val == value:
            return index
    return -1


assert linear_search(5, number_list) == 4
# print( linear_search(5, number_list) )

def linear_search_recusive(array, value):
    if len(array) == 0:
        return -1
    index = len(array) - 1
    if array[index] == value:
        return index
    return linear_search_recusive(array[0:index], value)


assert linear_search_recusive(number_list, 5) == 5
# print(linear_search_recusive(number_list, 5))

def binary_search(sorted_array, value):
    if not sorted_array:
        return -1
    begin = 0
    end = len(sorted_array) - 1
    while begin <= end:
        mid = (begin + end) // 2
        if sorted_array[mid] == value:
            return mid
        elif sorted_array[mid] > value:
            end = mid - 1
        else:
            begin = mid + 1
    return -1

def test_binary_search():
    a = list(range(10))
    assert binary_search(a, -1) == -1
    assert binary_search(a, 0) == 0
    assert binary_search(a, 9) == 9
    assert binary_search(None, 0) == -1
    
test_binary_search()