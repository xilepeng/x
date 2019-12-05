import random


def bubble_sort(seq):  # O(n^2), n(n-1)/2
    n = len(seq)
    for i in range(n - 1):  # 最后一轮已经有序，不需要比较
        print(seq)
        for j in range(n - 1 - i):  # 每一轮冒泡最大的元素都会冒泡到最后，无需再比较
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]

def test_bubble_sort():
    seq = list(range(10))
    random.shuffle(seq)
    bubble_sort(seq)
    assert seq == sorted(seq)

# test_bubble_sort()
"""
[9, 2, 6, 1, 5, 4, 0, 7, 8, 3]

[2, 6, 1, 5, 4, 0, 7, 8, 3, 9]
[2, 1, 5, 4, 0, 6, 7, 3, 8, 9]
[1, 2, 4, 0, 5, 6, 3, 7, 8, 9]
[1, 2, 0, 4, 5, 3, 6, 7, 8, 9]
[1, 0, 2, 4, 3, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""


def select_sort(seq):
    n = len(seq)
    for i in range(n - 1):  # 最后一位元素不需比较
        min_index = i   # 假设i是当前最小元素下标
        for j in range(i + 1, n):   # 从i的后面开始找到最小元素
            if seq[j] < seq[min_index]:
                min_index = j   # 一个j循环后就找到了最小元素的下标
        print(seq)
        if i != min_index:  # swap
            seq[min_index], seq[i] = seq[i], seq[min_index]

def test_select_sort():
    seq = list(range(10))
    random.shuffle(seq)
    select_sort(seq)
    assert seq == sorted(seq)
    # print(seq)

# test_select_sort()
"""
[9, 8, 4, 2, 3, 5, 6, 1, 0, 7]

[0, 8, 4, 2, 3, 5, 6, 1, 9, 7]
[0, 1, 4, 2, 3, 5, 6, 8, 9, 7]
[0, 1, 2, 4, 3, 5, 6, 8, 9, 7]
[0, 1, 2, 3, 4, 5, 6, 8, 9, 7]
[0, 1, 2, 3, 4, 5, 6, 8, 9, 7]
[0, 1, 2, 3, 4, 5, 6, 8, 9, 7]
[0, 1, 2, 3, 4, 5, 6, 8, 9, 7]
[0, 1, 2, 3, 4, 5, 6, 7, 9, 8]
"""
# def insertion_sort(seq):
#     n = len(seq)
#     print(seq,"\n")
#     for i in range(1, n):
#         pos = i
#         value = seq[i]  #记录当前位置值
#         while pos > 0 and value < seq[pos - 1]:
#             seq[pos] = seq[pos - 1] #将第一个数赋值给当前位置
#             pos -= 1    #当前位置前移
#         seq[pos] = value    #原当前位置赋给移动后的当前位置
#         print(seq)

def insertion_sort(seq):
    n = len(seq)
    for i in range(1, n):
        pos = i
        value = seq[i]
        while pos > 0 and value < seq[pos - 1]:
            seq[pos] = seq[pos - 1]
            pos -= 1
        seq[pos] = value
        print(seq)


def test_insertion_sort():
    seq = list(range(10))
    random.shuffle(seq)
    insertion_sort(seq)
    assert seq == sorted(seq)
    print()
    print(seq)

test_insertion_sort()
"""
[3, 0, 5, 6, 1, 4, 7, 8, 2, 9]

[0, 3, 5, 6, 1, 4, 7, 8, 2, 9]
[0, 3, 5, 6, 1, 4, 7, 8, 2, 9]
[0, 3, 5, 6, 1, 4, 7, 8, 2, 9]
[0, 1, 3, 5, 6, 4, 7, 8, 2, 9]
[0, 1, 3, 4, 5, 6, 7, 8, 2, 9]
[0, 1, 3, 4, 5, 6, 7, 8, 2, 9]
[0, 1, 3, 4, 5, 6, 7, 8, 2, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""