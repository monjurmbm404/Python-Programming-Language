"""
========================================
03_custom_iterator.py
========================================
Custom Iterator:

✔ Using class with __iter__ and __next__
"""

class MyNumbers:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 5:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration

obj = MyNumbers()
it = iter(obj)

for i in it:
    print(i)