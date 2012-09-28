class Foo(object):
    def __new__(self):
        return 'hello'

foo = Foo()

print type(foo), foo, repr(foo)
