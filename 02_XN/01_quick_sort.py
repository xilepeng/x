
def partition(nums, left, right):
    piviot = nums[left]
    while left < right:
        while left < right and nums[right] >= piviot:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= piviot:
            left += 1
        nums[right] = nums[left]
    nums[right] = piviot
    return right

def _quick_sort(nums, left, right):
    if left < right:    #待排序区至少有2个元素
        pivot = random_partition(nums, left, right)
        _quick_sort(nums, left, pivot - 1)
        _quick_sort(nums, pivot + 1, right)


def random_partition(nums, left, right):
    i = random.randint(left, right)
    nums[i], nums[left] = nums[left], nums[i]
    return partition(nums, left, right)

def quick_sort(nums):
    _quick_sort(nums, 0 , len(nums)-1)




def quick_sort2(nums):
    if len(nums) < 2:
        return nums
    pivot = nums[0]
    less_part = [v for v in nums[1:] if v <= pivot]
    great_part = [v for v in nums[1:] if v > pivot]
    return quick_sort2(less_part) + [pivot] + quick_sort2(great_part)



import random
nums = list(range(10))
random.shuffle(nums)
print(nums)
# quick_sort(nums)
print(quick_sort2(nums))












# #找出出现奇数次的数字
# nums = [1, 1, 2, 2, 3, 3, 5, 6, 6]
# result = 0 
# for value in nums:
#     result = result ^ value
# print(result)