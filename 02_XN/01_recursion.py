import functools

@functools.lru_cache(None)
def fib(n):
    if n < 2: 
        return 1
    return fib(n-1) + fib(n - 2)

print("斐波那契数列")
print(fib(100))


def fib2(n):
    li = [1, 1]
    for i in range(2, n + 1):
        li.append(li[-1]+li[-2])
    return li[n]

print(fib2(100))

def fib3(n):
    if n < 2:
        return 1
    a, b, c = 1, 1, 0
    for i in range(2, n + 1):
        c = a + b
        a, b = b, c   
    return c

print(fib3(100))      


def fib4(n):
    a, b, c = 1, 1, 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c     
    return c
    
print(fib4(100)) 


def hanoi(n, A, B, C):
    if n > 0:
        hanoi(n-1, A, C, B)
        print('%s->%s'%(A, C))
        hanoi(n-1, B, A, C)

print("汉诺塔")
hanoi(3, 'A', 'B', 'C')


















# 循环减半的过程-> O(logn)
# x层循环就是  -> O(n^x)
# 没有循环，O(1)


# O(1) < O(log n) < O(n)
# n每次少一个常数，时间复杂度：O(n)
# n每次减一半，时间复杂度：O(log n)
# n = 64
# while n > 1:
#     print(n)
#     n = n // 2

# 64
# 32
# 16
# 8
# 4
# 2
