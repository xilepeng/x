class Array(object):
    def __init__(self, size = 64, init = None):
        self._size = size
        self._items = [init] * size

    def __setitem__(self, index, value):
        self._items[index] = value

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return self._size

    def __iter__(self):
        for item in self._items:
            yield item

    def clear(self, value = None):
        for i in range(len(self._items)):
            self._items[i] = value

class Slot(object):
    """定义一个hash表的槽
    1.从未使用 HashMap.UNUSED, 此槽没有被使用和冲突过   
    2.使用过但是 remove 了，此时是 HashMap.EMPTY, 该探查点后面的元素仍可能有 key
    3.槽正在使用 Slot 节点
    """
    def __init__(self, key, value):
        self.key, self.value = key, value

class HashTable(object):
    UNUSED = None   # Slot 没被使用过
    EMPTY = Slot(None, None) # Slot 使用过但被删除了

    def __init__(self):
        self._table = Array(8, init=HashTable.UNUSED) # 初始化哈希表没使用过
        self.length = 0 # 已经使用槽的个数

    @property   # @property装饰器就是负责把一个方法变成属性调用
    def _load_factor(self):
        return self.length / float(len(self._table)) #使用长度除上哈希表总长度
    
    def __len__(self):
        return self.length #返回哈希表的长度

    def _hash(self, key):   # 哈希函数计算出槽下标
        return abs(hash(key))% len(self._table) 

    def _find_key(self, key):   # 寻找key
        index = self._hash(key)
        _len = len(self._table)
        while self._table[index] is not HashTable.UNUSED:
            if self._table[index] is HashTable.EMPTY:
                index = (index * 5 + 1) % _len  # 使用cpython 解决哈希冲突的方式
                continue
            elif self._table[index].key == key:
                return index
            else:
                index = (index * 5 + 1) % _len
        return None


    def _slot_can_insert(self, index):
        return (self._table[index] is HashTable.EMPTY or self._table[index] is HashTable.UNUSED)

    def _find_slot_for_insert(self, key):   # 寻找空槽
        index = self._hash(key)
        _len = len(self._table)
        while not self._slot_can_insert(index):
            index = (index * 5 + 1) % _len
        return index

    def __contains__(self, key):    # in operator 实现一个in 操作符
        index = self._find_key(key)
        return index is not None

    def add(self, key, value):
        if key in self:
            index = self._find_key(key)
            self._table[index].value = value
            return False
        else:
            index = self._find_slot_for_insert(key)
            self._table[index] = Slot(key, value)
            self.length += 1
            if self._load_factor >= 0.8:
                self._rehash()
            return True
    
    def _rehash(self):
        old_table = self._table
        newsize = len(self._table) * 2
        self._table = Array(newsize, HashTable.UNUSED)
        self.length = 0

        for slot in old_table:
            if slot is not HashTable.UNUSED and slot is not HashTable.EMPTY:
                index = self._find_slot_for_insert(slot.key)
                self._table[index] = slot
                self.length += 1
    
    def get(self, key, default = None):
        index = self._find_key(key)
        if index is None:
            return default
        else:
            return self._table[index].value

    def remove(self, key):
        index = self._find_key(key)
        if index is None:
            raise KeyError()
        value = self._table[index].value
        self.length -= 1
        self._table[index] = HashTable.EMPTY
        return value

    def __iter__(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                yield slot.key


#########################################
# 上边是从 哈希表章 拷贝过来的代码，我们会直接继承 HashTable 实现 dict
#########################################

class DictADT(HashTable):

    def __setitem__(self, key, value):
        self.add(key, value)
    
    def __getitem__(self, key):
        if key not in self:
            raise KeyError()
        else:
            return self.get(key)

    def _iter_slot(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                yield slot

    def items(self):
        for slot in self._iter_slot():
            yield (slot.key, slot.value)
    
    def keys(self):
        for slot in self._iter_slot():
            yield slot.key

    def value(self):
        for slot in self._iter_slot():
            yield slot.value

def test_dict_adt():
    import random
    d = DictADT()

    d['a'] = 1
    assert d['a'] == 1
    d.remove('a')

    l = list(range(30))
    random.shuffle(l)
    for i in l:
        d.add(i, i)

    for i in range(30):
        assert d.get(i) == i

    assert sorted(list(d.keys())) == sorted(l)

    
