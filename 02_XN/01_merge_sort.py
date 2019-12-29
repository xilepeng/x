
def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    mid = len(seq) // 2
    left = merge_sort(seq[ : mid])
    right = merge_sort(seq[mid : ])
    result = merge_sorted_list(left, right)
    return result

def merge_sorted_list(sorted_a, sorted_b):
    length_a, length_b = len(sorted_a), len(sorted_b)
    a = b = 0
    result = list()
    while a < length_a and b < length_b:
        if  sorted_a[a] < sorted_b[b]:
            result.append(sorted_a[a])
            a += 1
        else:
            result.append(sorted_b[b])
            b += 1
    if a < length_a:
        result.extend(sorted_a[a:])
    else:
        result.extend(sorted_b[b:])
    # while a < length_a:
    #     result.append(sorted_a[a])
    #     a += 1
    # while b < length_b:
    #     result.append(sorted_b[b])
    #     b += 1
    return result

import random
seq = list(range(10))
random.shuffle(seq)
print(merge_sort(seq))

sorted_a = list(range(5))
sorted_b = list(range(5,11))

# print( merge_sorted_list(sorted_a, sorted_b) )


