def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

# print(fact(10))

def print_num_recursive(n):
    if n >0 :
        
        print_num_recursive(n-1)
        print(n)

# print_num_recursive(10)


from collections import deque

class Stack (object):

    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop (self):
        return self._deque.pop()

    def is_empty(self):
        return len(self._deque) == 0

def print_num_use_stack(n):
    s = Stack()
    while n > 0:
        s.push(n)
        n -= 1
    while not s.is_empty():
        print(s.pop())

print_num_use_stack(10)






























# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n - 1)
# # print(fact(3))

# def print_num(n):
#     for i in range(1,n + 1):
#         print(i)
# # print_num(10)

# def print_num_recursive(n):
#     if n > 0:
#         print_num_recursive(n - 1)
#         print(n)
# # print_num_recursive(10)
# # 尾递归：倒序
# def print_num_recursive1(n):
#     if n > 0:
#         print(n)
#         print_num_recursive1(n - 1)
# # print_num_recursive1(10)

# # 用栈模拟递归
# from collections import deque
# class Stack(object):
#     def __init__(self):
#         self._deque = deque()
#     def push(self, value):
#         return self._deque.append(value)
#     def pop(self):
#         return self._deque.pop()
#     def is_empty(self):
#         return len(self._deque) == 0
# def print_num_use_stack(n):
#     s = Stack()
#     while n > 0:
#         s.push(n)
#         n -= 1
#     while not s.is_empty():
#         print(s.pop())

# print_num_use_stack(10)

# # watchtest pytest -s x.py