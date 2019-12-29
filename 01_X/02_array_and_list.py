# 定长数组
class Array(object):
    def __init__(self, size = 64):
        self._size = size
        self._items = [None]*size

    def __setitem__(self, index, value):
        self._items[index] = value

    def __getitem__(self,index):
        return self._items[index]
    
    def __len__(self):
        return self._size

    def __iter__(self):
        for item in self._items:
            yield item

    def clear(self, value = None):
        for i in range(len(self._items)):
            self._items[i] = value

def test_array():
    size = 522
    a = Array(size)
    a[0] = 98
    a[1] = 100
    assert a[0] ==98
    assert a[1] == 100
    assert len(a) == 522
    a.clear()
    assert a[0] is None


test_array()




# from array import array

# arr = array('u', 'xilepeng')
# # print(arr[0], arr[1], arr[2])

# class Array(object):
#     def __init__(self, size=32):
#         self._size = size   #视为私有变量，不要随意访问
#         self._items = [None] * size

#     def __getitem__(self, index):
#         return self._items[index]

#     def __setitem__(self, index, value):
#         self._items[index] = value
    
#     def __len__(self):
#         return self._size

#     def clear(self, value = None):
#         for i in range(len(self._items)):
#             self._items[i] = value

#     def __iter__(self):
#         for item in self._items:
#             yield item  #遇到yield就中断，下次又继续执行。
#     #generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。


# def test_array():
#     size = 10
#     a = Array(size)
#     a[0] = 1
#     assert a[0] == 1
#     assert len(a) == 10
#     a.clear()
#     assert len(a) == 10
#     assert a[0] is None

# test_array()

