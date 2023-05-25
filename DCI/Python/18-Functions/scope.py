def create_list(my_default=[]):
    my_default.append(1)
    my_list = []
    for i in range(5):
        my_list.append(i)
    print('INSIDE', locals())
    return my_list

create_list()
# print(create_list.__defaults__)
print('OUT', locals())