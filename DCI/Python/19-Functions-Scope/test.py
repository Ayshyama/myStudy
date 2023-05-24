def my_function(a, b, **kwargs):
    print(kwargs)
    kwargs.get('loc', 'empty')

my_function(1,2)

def my_function(a, b, **kwargs):
    print(kwargs)
    print(kwargs.get('loc', 'empty'))

my_function(1,2)

def my_function2(x, y, loc=None, color=None, **kwargs):
    print(loc)
    print(kwargs.get('loc', 'empty'))

my_function(1,2, loc='Bla')
my_function2(1,2, loc='Bla')
my_function(1,2, loc='Bla', size=10)




