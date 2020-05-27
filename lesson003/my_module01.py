def add(x, y):
    return x + y

# 只在当前文件中调用改函数，其他导入的文件呢不符合该条件，则不执行add函数
if __name__ == "__main__":
    print(add(1, 2))
