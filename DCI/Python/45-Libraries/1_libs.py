import builtins


def check_variable(symbol):
    print(f'Local Namespace: {symbol}', locals().get(symbol))
    print('-------')
    print(f'Global Namespace: {symbol}', globals().get(symbol))
    print('-------')
    print(vars(builtins).get(symbol))
    print('-------')


# print(sum([1, 2, 3]))
#
# sum = 'bla_global'
#
# check_variable('sum')

# sum = 'bla_global'

my_new_sum = vars(builtins).get('sum')
print(my_new_sum([1, 2, 3]))


sum = my_new_sum


def outer():
    sum = 'nonlocal hello'

    def inner():
        nonlocal sum
        print(sum)
        print(globals().get('sum'))
        sum = globals().get('sum')
        print('inner but global', sum([1, 2, 3]))
        print(locals().get('sum'))

    inner()


outer()

print(dir(__builtins__))

print('sum' in dir(__builtins__))

