#快速添加数据
ls = [1,2,3,4]
list1 = [i for i in ls if i > 2]
print(list1)
list2 = [i * 2 for i in ls if i > 2]
print(list2)
tuple1 = (2,4,6)
dict1 = {x: x**2 for x in tuple1}
dict2 = {x: 'item' + str(x**2) for x in tuple1}
print(dict1)
print(dict2)
