import random

nums = list(range(10))
random.shuffle(nums)
n = len(nums)

# 最好情况 O(n), 平均情况 O(n^2), 最坏情况 O(n^2)
# 稳定
def bubble_sort(nums):
    for i in range(n-1):    # i 表示第n趟 
        exchange = False
        for j in range(n-1-i):  # 第i趟 无序区[0, n-i-1] j表示箭头 0 ~ n-i-2
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                exchange = True
        if not exchange :
            break
    
def test_bubble_sort():
    sorted_nums = sorted(nums)
    assert bubble_sort(nums) == sorted_nums

def get_min_pos(nums):
    min_pos = 0
    for i in range(1, n):
        if nums[i] < nums[min_pos]:
            pos = i
    return min_pos


# 不稳定
def select_sort(nums):
    for i in range(n-1):
        print(nums)
        min_index = i
        for j in range(i+1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]
    

# select_sort(nums)

def insert_sort(nums):
    print(nums)
    for i in range(1, n):
        value = nums[i]
        pos = i
        while pos > 0 and nums[pos-1] > value:  #前面的元素比value大
            nums[pos] = nums[pos -1]
            pos -= 1
        nums[pos] = value
        print(nums)

insert_sort(nums)
