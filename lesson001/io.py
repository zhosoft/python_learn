fo = open('test.txt', 'wt')
fo.write("www.baidu.com!\nVery good site!\n")
read_content = fo.read()
print(read_content)
fo.close()
