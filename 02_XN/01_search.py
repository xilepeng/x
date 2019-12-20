
# O(n)
def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i

def test_linear_search():
    nums = [1, 4, 5, 8, 9]
    assert linear_search(nums, 5) == 2


# O(log n)
def binary_search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:  #nums[0,n]非空，继续寻找
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def test_binary_search():
    nums = [1, 4, 5, 8, 9]
    assert binary_search(nums, 5) == 2



def bin_search_rec(nums, target, low, high):
    mid = (low + high) // 2
    if low <= high:
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            bin_search_rec(nums, target, low, mid - 1)
        else:
            bin_search_rec(nums, target, mid + 1, high)
    else:
        return -1

def test_bin_search_rec():
    nums = [1, 4, 5, 8, 9]
    assert bin_search_rec(nums,5, 0, len(nums)-1) == 2