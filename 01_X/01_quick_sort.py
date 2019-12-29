"""
快排是一种分治策略，归并排序是把数组递归成只有单个元素的数组，之后再不断两两合并
，最后得到一个有序数组。这里的递归基本条件就是只包含一个元素的数组，当数组只包含
一个元素的时候，我们可以认为他本来就是有序的。
"""
def quick_sort(array):
    """
    1. 选择基准值 pivot 将数组分成两个子数组：小于基准值的元素和大于基准值的元素，这个
    过程称为分组 partition。
    2. 对这两个子数组进行快速排序。
    3. 合并结果。
    """
    if len(array) < 2:
        return array
    else:
        pivot_index = 0
        pivot = array[pivot_index]
        less_part = [i for i in array[pivot_index + 1:] if i <= pivot]
        great_part = [i for i in array[pivot_index + 1:] if i > pivot]
        return quick_sort(less_part) + [pivot] + quick_sort(great_part)



def partition(array, begin, end):
    pivot_index = begin
    pivot = array[pivot_index]
    left, right = begin + 1, len(array) - 1
    while True:
        while left <= right and array[left] <= pivot:
            left += 1
        while left <= right and array[right] >= pivot:
            right -= 1
        if left > right:
            break
        else:
            array[left], array[right] = array[right], array[left]
    array[pivot_index], array[right] = array[right], array[pivot_index]
    return right

def quicksort_inplace(array, begin, end):
    if begin < end :
        pivot = partition(array, begin, end)
        quicksort_inplace(array, begin, pivot)
        quicksort_inplace(array, pivot + 1, end)
    

if __name__ == "__main__":
    import random

    seq = list(range(10))
    random.shuffle(seq)
    print(seq)
    # print(quick_sort(seq))
    quicksort_inplace(seq, 0, len(seq))
    print(seq)
    # print(sorted(seq))

# def test_quick_sort():
#     import random
#     seq = list(range(10))
#     random.shuffle(seq)
#     assert quick_sort(seq) == sorted(seq)

# if __name__ == '__main__':
#     test_quick_sort()
