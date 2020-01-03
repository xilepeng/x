<<<<<<< HEAD
from bisect import bisect
nums = [1, 3, 5, 6, 8]


def binary_search(nums, target):
    """简单二分模版"""
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left + right)//2
        if target == nums[mid]:
            return mid
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

# print(binary_search(nums, 5))


alist = [1, 2, 5, 5, 5, 6, 7]


def findDuplicate(alist, item):
    """寻找第一个重复数下标"""
    if len(alist) == 0:
        return -1
    left, right = 0, len(alist)-1
    while left+1 < right:   # LR (LR) RL 相邻重叠相交，退出循环体
        mid = left + (right-left) // 2
        if alist[mid] == item:
            right = mid  # 查看左半边，找到第一个重复数
=======

def binary_search(alist, item):
    """查找第一个重复元素下表"""
    if len(alist) == 0:
        return -1
    left, right = 0, len(alist)-1
    while left+1 < right:   # LR  (LR)  RL  相邻，重叠，相交： 跳出循环体
        mid = left + (right-left) // 2
        if alist[mid] == item:
            right = mid
>>>>>>> master
        elif alist[mid] > item:
            right = mid
        elif alist[mid] < item:
            left = mid
<<<<<<< HEAD

    if alist[left] == item:  # LR相邻   2 2  1 2  2 3  3 3
        return left
    if alist[right] == item:
        return right
    return -1


# print(findDuplicate(alist, 5))


nums = [3, 4, 5, 1, 2]


def findMin(nums):
    """leetcode 153. 寻找旋转排序数组中的最小值 O(lg n)"""
    if len(nums) == 0:
        return -1
    left, right = 0, len(nums) - 1
    while left + 1 < right:  # left right 相邻退出
        if nums[left] < nums[right]:    # nums有序
            return nums[left]
        mid = left + (right - left) // 2
        if nums[mid] >= nums[left]:  # 前半部分排好序的，到后半部分找
            left = mid + 1
        else:
            right = mid
    return nums[left] if nums[left] < nums[right] else nums[right]

# print(findMin(nums))


def findMin2(nums):
    """leetcode 153. 寻找旋转排序数组中的最小值 O(lg n)"""
    left, right = 0, len(nums) - 1
    while left < right:  # left==right退出
        mid = (left + right) // 2
        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1
    return nums[left]

# print(findMin2(nums))


nums = [4, 5, 6, 7, 0, 1, 2]


def search(nums, target):
    """leetcode 33. 搜索旋转排序数组"""
    if len(nums) == 0:
        return -1
    left, right = 0, len(nums)-1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] < nums[mid]:
            if nums[left] <= target and target <= nums[mid]:
                right = mid
            else:
                left = mid
        else:
            if nums[mid] <= target and target <= nums[right]:
                left = mid
            else:
                right = mid
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return -1
# print(search(nums, 0))


def search2(nums, target):
    """leetcode 33. 搜索旋转排序数组"""
    for key, value in enumerate(nums):
        if value == target:
            return key
    return -1


nums = [1, 3, 5, 6]


def searchInsert(nums, target):
    """leetcode 35. 搜索插入位置"""
    begin, end = 0, len(nums) - 1
    while begin <= end:  # end,begin 相交退出0，1
        mid = (begin + end) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            end = mid - 1
        else:
            begin = mid + 1
    return begin

# print(searchInsert(nums, 2))


def searchInsert(nums, target):
    """leetcode 35. 搜索插入位置:找到第一个大于等于的值"""

    if len(nums) == 0:
        return 0
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            left = mid
        else:
            right = mid
    if nums[left] >= target:
        return left
    if nums[right] >= target:
        return right
    return right + 1

# print(searchInsert(nums, 2))


nums = [1, 2, 2, 2, 2, 3, 4, 5, 8]
# O(lg n)


def search_range(nums, target):
    """搜索重复数字区间:找到目标值的开始结束位置"""
    if len(nums) == 0:
        return (-1, -1)
    lbound, rbound = -1, -1
    # 找左边界
    left, right = 0, len(nums)-1
    while left + 1 < right:
        mid = (left + right)//2
        if nums[mid] == target:
            right = mid
        elif target < nums[mid]:
            right = mid
        else:
            left = mid
    if nums[left] == target:
        lbound = left
    elif nums[right] == target:
        lbound = right
    else:
        return (-1, -1)

    # 找右边界
    left, right = 0, len(nums)-1
    while left + 1 < right:
        mid = (left + right)//2
        if nums[mid] == target:
            left = mid
        elif target < nums[mid]:
            right = mid
        else:
            left = mid
    if nums[right] == target:
        rbound = right
    elif nums[left] == target:
        rbound = left
    else:
        return [-1, -1]

    return [lbound, rbound]

# print(search_range(nums, 2))


# 茫茫人海，我们相遇了！
# 愿你眼里都是阳光，笑里全是坦荡；
# 愿你此生尽兴，赤诚善良；
# 愿我虔诚的祝福，带给你成功的一年。
# 祝徐楠生日快乐!

# O(n)
alist = [1, '', '', 3, '', '', 4, '', '', 5]


def search_empty(alist, target):
    """Search in Sorted Array with Empty Strings"""
    for key, value in enumerate(alist):
        if value == target:
            return key
    # if len(alist) == 0:
    #     return -1
    # left, right = 0, len(alist) - 1
    # while left + 1 < right:
    #     # 找到右边第一个非空数字
    #     while left+1 < right and alist[right] == "":
    #         right -= 1
    #     if alist[right] == "":
    #         right -= 1
    #     if left > right:
    #         return -1

    #     mid = (left + right)// 2
    #     while alist[mid] == "":
    #         mid += 1
    #     if alist[mid] == target:
    #         return mid
    #     if alist[mid] < target:
    #         left = mid + 1
    #     else:
    #         right = mid - 1
    # if alist[left] == target:
    #     return left
    # if alist[right] == target:
    #     return right

    return -1

# print(search_empty(alist, 5))


alist = [0, 0, 0, 0, 0, 1]


def search_first(alist):
    """在无限序列中找到某元素的第一个出现位置，sort, 数据流:不知道数据长度"""
    left, right = 0, 1
    while alist[right] == 0:
        left = right
        right *= 2

        if (right > len(alist)):
            right = len(alist)-1
            break
    return left + search_range(alist[left:right+1], 1)[0]


def findRadius( houses, heaters):
    heaters.sort()
    ans = 0
    for h in houses:
        hi = bisect(heaters, h)
        # res = bisect(sorted_nums,value)    第一个大于等于h的位置，应插入有序数组的位置
        left = heaters[hi-1] if hi-1 >= 0 else float('-inf')
        right = heaters[hi] if hi < len(heaters) else float('inf')
        ans = max(ans, min(h - left, right - h))
    return ans


def mySqrt(x):
    """69. x 的平方根"""
    if x == 0:
        return 0
    left, right = 1, x
    while left <= right:
        mid = (left + right) // 2
        if (mid == x // mid):
            return mid
        if (mid < x // mid):
            left = mid + 1
        else:
            right = mid - 1
    return right


# print(mySqrt(4))
=======
        
    if alist[left] == item:
        return left
    if alist[right] == item:
        return right
    return -1 

alist = [1, 2, 3, 5, 5, 5, 6, 7]
res = binary_search(alist, 5)
print(res)
>>>>>>> master
