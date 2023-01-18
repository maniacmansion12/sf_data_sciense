i = 5
print(isinstance(i, object))
True
print(isinstance('Oo', object))
True
print(isinstance([2, 4, 't'], object))
True
print(isinstance({'a': 3, 'b': 5}, object))
True
print(isinstance((2, 4, 'w'), object))
True
def test_func():
    pass
print(isinstance(test_func, object))
True