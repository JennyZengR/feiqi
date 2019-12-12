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

#将不符合条件的字符去掉
set1 = {x for x in "hello world" if x not in "low level"}
print(set1)

#去重
#1。利用set不可重复
a = [1, 2, 4, 2, 4, 5, 6, 5, 7, 8]
a1 = set(a)
b1 = list(a1)
print(a1)
print(b1)
#2。利用dict不可重复
b = {}
#list转换成字典需要用字典的fromkeys（）方法
#由于list在迭代的时候没有只有一个值，所以不能直接使用dict(li)把列表转换为字典。在这里我们需要使用字典里的fromkeys()方法。
#fromkeys() ：函数用于创建一个新字典，列表中的元素当做key，并为每个key设置一个固定值（value是可选的，如果没有默认为None）。
b = b.fromkeys(a)
print(b)
c = list(b.keys())
print(c)