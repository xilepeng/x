def merge_sort(seq):
    if len(seq) <= 1:  # 递归出口
        return seq
    else:
        mid = len(seq) // 2
        left_half = merge_sort(seq[:mid])
        right_half = merge_sort(seq[mid:])
        new_seq = merge_sorted_list(left_half, right_half)
        print(new_seq)
    return new_seq


def merge_sorted_list(sorted_a, sorted_b):
    """合并2个有序序列，返回一个新的有序序列"""
    length_a, length_b = len(sorted_a), len(sorted_b)
    a = b = 0
    new_sorted_seq = list()
    while a < length_a and b < length_b:
        if sorted_a[a] < sorted_b[b]:
            new_sorted_seq.append(sorted_a[a])
            a += 1
        else:
            new_sorted_seq.append(sorted_b[b])
            b += 1
    if a < length_a:
        new_sorted_seq.extend(sorted_a[a:])
    else:
        new_sorted_seq.extend(sorted_b[b:])
    return new_sorted_seq


def test_merge_sort():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    merge_sort(seq)
    assert merge_sort(seq) == sorted(seq)


# test_merge_sort()

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot_index = 0
        pivot = array[pivot_index]
        less_part = [i for i in array[pivot_index + 1:] if i <= pivot]
        great_part = [i for i in array[pivot_index + 1:] if i > pivot]
        return quick_sort(less_part) + [pivot] + quick_sort(great_part)


def test_quick_sort():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    print(quick_sort(seq))
    assert quick_sort(seq) == sorted(seq)


# test_quick_sort()

def quick_sort_inplace(array, begin, end):
    if begin < end:
        pivot = partiton(array, begin, end)
        quick_sort_inplace(array, begin, pivot)
        quick_sort_inplace(array, pivot+1, end)

def partiton(array, begin, end):
    pivot_index = begin
    pivot = array[pivot_index]
    left = pivot_index + 1
    right = end - 1
    while True:
        while left <= right and array[left] < pivot:
            left += 1
        while left <= right and array[right] > pivot:
            right -= 1
        if left > right:
            break
        else:
            array[left], array[right] = array[right], array[left]
    array[right], array[pivot_index] = array[pivot_index], array[right]
    return right

def test_quick_sort_inplace():
    import random
    l = list(range(10))
    random.shuffle(l)
    quick_sort_inplace(l, 0, len(l))
    # assert quick_sort_inplace(l, 0, len(l)) == sorted(l)
    print(l)

test_quick_sort_inplace()