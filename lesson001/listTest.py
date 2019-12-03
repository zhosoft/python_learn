# list = ['ZHANGS','KLU','JKHASJDFK']
#
# print(len(list))
# print(list) #['ZHANGS','KLU','JKHASJDFK']
# print(list[1])#KLU
# print(list[0:1]) #['ZHANGS','KLU']
# del list[1]
# print(list) #['ZHANGS','JKHASJDFK']
# print(len(list))
# print(max(list))


# brith_year = input('Birth year: ')
#
# print(type(brith_year))
#
# age = 2019 - int(brith_year)
#
# print(age)


name_list = ['zhangsan', 'Tom', 'Rose',"zhangsan",123]
#
# print(name_list.index('Tom', 0, 2))
#
# print(name_list.count('zhangsan'))
#
# print(len(name_list))
#
# print("Tom" in name_list)
# print("a" in name_list)
#
# keyword = input("please input search keyworks\n")
#
# if keyword in name_list:
#     print(f"yes，{keyword},存在")
# else:
#     print(f"no，{keyword},不存在")


print(name_list)

name_list.append("wangwu")

print(name_list)

name_list.extend("xiao")

print(name_list)

name_list.insert(2,"3333")

print(name_list)
