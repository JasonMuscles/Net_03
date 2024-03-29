from collections import Iterable
from collections import Iterator
import time


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果想让对象可迭代对象，可使用for，那么必须实现__iter__方法"""
        return ClassIterator(self)


class ClassIterator(object):
    def __init__(self, obj):
        self.obj = obj
        self.current_num = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.current_num < len(self.obj.names):
            ret = self.obj.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration


classmate = Classmate()

classmate.add("老大")
classmate.add("老二")
classmate.add("老三")

# print("判断classmate是否是可以迭代的对象：", isinstance(classmate, Iterable))
#
# classmate_iterator = iter(classmate)
# print("判断classmate是否是迭代器：", isinstance(classmate_iterator, Iterator))

for name in classmate:
    print(name)
    time.sleep(1)
