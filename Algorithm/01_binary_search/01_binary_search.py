
def binary_search(alist, item):
    """查找第一个重复元素下表"""
    if len(alist) == 0:
        return -1
    left, right = 0, len(alist)-1
    while left+1 < right:   # LR  (LR)  RL  相邻，重叠，相交： 跳出循环体
        mid = left + (right-left) // 2
        if alist[mid] == item:
            right = mid
        elif alist[mid] > item:
            right = mid
        elif alist[mid] < item:
            left = mid
        
    if alist[left] == item:
        return left
    if alist[right] == item:
        return right
    return -1 

alist = [1, 2, 3, 5, 5, 5, 6, 7]
res = binary_search(alist, 5)
print(res)