class A (object):
    data = 522
    def fun1(self):
        print('fun1')
    @classmethod
    def fun2(cls):
        """classmethod 修饰符对应的函数不需要实例化，
        不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，
        可以来调用类的属性，类的方法，实例化对象等。"""
        print("fun2")
        print(cls.data)
        cls().fun1() # 调用fun1

A.fun2()    #不需要实例化
