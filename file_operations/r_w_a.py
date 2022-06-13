'''
r模式 以只读模式打开
read()、read(n)、readline()、readlines()等方法读取
'''
f = open("alex自述", encoding="utf-8", mode="r")  # mode不写默认是读
content = f.read()   # 全部读取
content = f.read(4)   #  按照字符读取
content = f.readline()  #  一行一行读取
content = f.readlines()  # 返回一个列表，列表中的每个元素是源文件的每一行
f.close()

# for循环读取
f = open("alex自述", encoding="utf-8", mode="r")
for content in f:
    print(content)
f.close()

"""
w模式  以写方式打开
没有文件，创建文件，写入内容
文件存在，先清空原文件内容，在写入新内容
"""
f = open("alex自述", encoding="utf-8", mode="w")
f.write("15802682581")
f.close()

'''
a模式  以追加模式打开
没有文件，创建文件，追加内容
文件存在，那么它会在原文件的最后面追加内容
'''
f = open("alex自述", encoding="utf-8", mode="a")
f.write("15802681852"+"\n")
f.close()
