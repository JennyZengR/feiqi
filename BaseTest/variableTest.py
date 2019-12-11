#将对象转换成字符串 repr
b = {"name":"linda","age":18}
str_b = repr(b)
print(str_b[0:3])

#截取字符串中的某几位
a = "happy new year"
print(a[1:4])

#把字符串转换成列表 eval
c = "[1,2,3]"
list_c = eval(c)
print(list_c)
print(list_c[0])

#格式输出
print("Hi %s,you have $%d." %("linda",100000))
#保留小数点后1位
print("hello,{0},{1:.1f}".format("linda",17.123))
#设置指定位置，按默认顺序
print("{0} {2}".format("hello","world","python"))
#不设置指定位置，按默认顺序
print("{} {}".format("hello","world","python"))