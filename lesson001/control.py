# import math
# print(math.pi)
# if 语句
x = 10
if x < 0:
    print('x小于0')
elif x == 10:
    print('x等于10')
else:
    print('default')

# 定义数组
words = ['cat', 'window', 'pig']
# for循环
for w in words:
    print(w, '===长度： ' + str(len(w)))

# range()

for i in range(5, 10):
    print(i)

print(list(range(5)))


def person():
    age = 30
    name = 'zhangsan'
    sex = 'nan'
    if age < 40:
        name = 'lisi'
    return name + sex + str(age)


print(person())


