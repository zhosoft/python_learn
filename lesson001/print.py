# 1.注释
# 2.打印
# 3.常用的数据类型 int str double
# 4.数据类型转换 str() int() double()
# 5.定义变量，并获取变量的数据类型 type()
# 6.字符串拼接 "+"

# 注释
print(100)
print('zhangsan')
print("程序员")
print('''11 
kjklf''')

# 定义变量
print("#####################")
name = 'zhangsan'
print(name)

age = '20'
print(age)
print(type(age))
print(int(age))

print("##############################")
# 字符串拼接

name = '张三丰'
sex = "男"
age = 30

print("姓名：" + name + "，性别：" + sex + "，年龄：" + str(age))
print("姓名：" + name + "，性别：" + sex + "，年龄：" + '30')