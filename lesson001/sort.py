list = [1, 5, 3, 6, 10, 24, 99, 54]

def sortport(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j]=list[j+1]
                list[j+1] = temp
                # [1, 3, 5, 6, 10, 24, 54, 99]
                # list[j], list[j + 1] = list[j + 1], list[j]
    return list

print(sortport(list))