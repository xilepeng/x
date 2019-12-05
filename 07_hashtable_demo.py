inserted_index_set = set()
M = 13

def h(key, M=13):
    return key % M

to_insert = [765, 431, 96, 142, 579, 226, 903, 388]
for number in to_insert:
    index = h(number)
    first_index = index
    i = 1
    while index in inserted_index_set:
        print('\th({number}) = {number} % M = {index} collision'.format(number=number, index=index))
        index = (first_index + i*i) % M
        i += 1
    else:
        print('h({number}) = {number} % M = {index}'.format(number=number, index=index))
        inserted_index_set.add(index) # 槽 index冲突，而不是数值number冲突




# inserted_index_set = set()
# M = 13

# def h(key, M=13):
#     return key % M

# to_insert = [765, 431, 96, 142, 579, 226, 903, 388]
# for number in to_insert:
#     index = h(number)
#     first_index = index
#     i = 1
#     while index in inserted_index_set:  # 如果槽已经被占用，继续计算得到下一个可用槽位置
#         print('\th({number}) = {number} % M = {index} collision'.format(number=number, index=index))
#         index = (first_index + i * i) % M  # 根据二次探查公式重新计算下一个需要插入的位置
#         i += 1
#     else:
#         print('h({number}) = {number} % M = {index}'.format(number=number, index=index))
#         inserted_index_set.add(index)



#         h(765) = 765 % M = 11
#         h(431) = 431 % M = 2
#         h(96) = 96 % M = 5
#         h(142) = 142 % M = 12
#         h(579) = 579 % M = 7
#         h(226) = 226 % M = 5 collision
#         h(226) = 226 % M = 6
#         h(903) = 903 % M = 6 collision
#         h(903) = 903 % M = 7 collision
#         h(903) = 903 % M = 10
#         h(388) = 388 % M = 11 collision
#         h(388) = 388 % M = 12 collision
#         h(388) = 388 % M = 2 collision
#         h(388) = 388 % M = 7 collision
#         h(388) = 388 % M = 1
# 插入 765, 431, 96, 142, 579, 226, 903, 388 到长度 M=13 的哈希表
#  0   1   2   3   4   5   6   7   8   9   10  11  12
# ————————————————————————————————————————————————————
#     388 431         96  226 579          903 765 142      二次探查后插入结果
# ————————————————————————————————————————————————————
#         388         226 903 903              388 388      冲突
#                             388
