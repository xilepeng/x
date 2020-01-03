

def binary_search(nums, target):
    """二分查找"""
    begin, end = 0, len(nums) - 1
    while begin <= end:
        mid = begin + (end - begin)// 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            begin = mid + 1
        else:
            end = mid - 1
    return -1


def binary_search_rec(nums, target):
    """二分查找,递归"""
    begin, end = 0, len(nums) - 1
    while begin <= end:
        mid = begin + (end - begin)// 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            binary_search_rec(nums[mid+1:],target)
        else:
            binary_search_rec(nums[:mid-1],target)
    return -1



# def binary_search(sorted_array, target):
#     begin, end = 0, len(sorted_array)-1
#     mid = begin + (end - begin) // 2
#     while begin <= end:
#         if sorted_array[mid] == target:
#             return target
#         if sorted_array[mid] < target:
#             begin = mid + 1
#         else:
#             end = mid - 1
#     return -1


def test_binary_search():
    a = list(range(1,10))
    assert binary_search(a, 1) == 1
    assert binary_search_rec(a, 2) == 2

test_binary_search()           

number_list = [0, 1, 2, 3, 4, 5, 6, 7]

def linear_search(value, iterable):
    for index, val in enumerate(iterable):
        if val == value:
            return index
    return -1

assert linear_search(5, number_list) == 5

# 传一个函数
def linear_search_v2(predicate, iterable):
    for index, val in enumerate(iterable):
        if predicate(val):
            return index
    return -1

assert linear_search_v2(lambda x : x==5, number_list) == 5


# def fun1(x,y):
#     return x+y
# assert fun1(2,3) == 5

# fun2 = lambda x,y: x+y
# assert fun2(2,3) == 5

# result = list(map(fun2,[2,2],[3,1]))
# print(result)

# 递归
def linear_search_recusive(array, value):
    if len(array) == 0:
        return -1
    index = len(array) - 1
    if array[index] == value:
        return index
    return linear_search_recusive(array[0:index],value)

assert linear_search_recusive(number_list, 5)== 5
    


# number_list = [0, 1, 2, 3, 5, 5, 6, 7]

# def linear_search(value, iterable):
#     for index, val in enumerate(iterable):
#         if val == value:
#             return index
#     return -1


# assert linear_search(5, number_list) == 4
# # print( linear_search(5, number_list) )

# def linear_search_recusive(array, value):
#     if len(array) == 0:
#         return -1
#     index = len(array) - 1
#     if array[index] == value:
#         return index
#     return linear_search_recusive(array[0:index], value)


# assert linear_search_recusive(number_list, 5) == 5
# # print(linear_search_recusive(number_list, 5))

# def binary_search(sorted_array, value):
#     if not sorted_array:
#         return -1
#     begin = 0
#     end = len(sorted_array) - 1
#     while begin <= end:
#         mid = (begin + end) // 2
#         if sorted_array[mid] == value:
#             return mid
#         elif sorted_array[mid] > value:
#             end = mid - 1
#         else:
#             begin = mid + 1
#     return -1

# def test_binary_search():
#     a = list(range(10))
#     assert binary_search(a, -1) == -1
#     assert binary_search(a, 0) == 0
#     assert binary_search(a, 9) == 9
#     assert binary_search(None, 0) == -1
    
# test_binary_search()