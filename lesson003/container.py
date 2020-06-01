# 容器：列表、元组、字典、集合

# 一、列表：['张三'，11，1.0]
# 列表可以嵌套列表
# 向列表中添加元素：列表.append()
# 向列表的指定位置添加元素：列表.inster(index,object)
# 向一个列表中添加另外一个列表的所有元素 列表.extend(新列表)
# 使用+号拼接2个列表，组成新的列表
# 切片：左边右开

# 二、元组
# 元组与列表类似：
# 【相同点】都可以存储相同类型或者不同类型的元素
# 【不同点】元组一旦被定义，只有不可以再修改元组内的元素，元组不支持添加、修改、删除元素操作
# 定义：(1,2,3)

# 三、字典
# 主要用于存储 key-value键值对 {}
# dict.get(key值)  如果key存在，返回对应的value，否则返回None空类型，并且程序不会报错。如果不想返回None空类型，则通过get方法的第二个参数，可以设置默认值。
# dict.key();dict.value(); 两个不能同时使用
# dict.item() ;将键值对转换为元组

# 四、集合
# 集合使用一对{}定义，与字典定义使用的符合相同，但是集合内存储的值不是键值对，是一个独立的数值
# set.add()添加
# set.update() 更新
# set.remove() 删除
# set.discard() 删除集合中指定的元素，如果要删除的元素不存在，也不会引发错误。
# set.pop() 随机删除集合中的某个元素，并返回删除的元素。
# 集合的交集 intersection() 、集合的并集union()、集合的差集difference()

##列表##
name_list = ['张三', 11, 'lisi', 10.12, [11.11, 'lisi']]
for value in name_list:
    print(value)

name_list.append('age')
for value in name_list:
    print(value)

print('==========')
name_list.insert(1, 'name')

for value in name_list:
    print(value)

print('==========')
name_list2 = ['book', 'number', 100]
name_list.extend(name_list2)

for value in name_list:
    print(value)

print('==========')

new_list = name_list + name_list2
for value in new_list:
    print(value)

## 元组 ##

tp = (1, 2, 3)

for value in tp:
    print(value)

print(type(tp))  # tuple

## 字典 ##

dict = {'name': '张三', 'age': 30, 'gender': 'name'}

print(dict.get('age1', 20))  # 30
print(type(dict))  # dict

keys = dict.keys()
for key in keys:
    print(key)

values = dict.values()
for value in values:
    print(value)

items = dict.items()
for item in items:
    print(item)
