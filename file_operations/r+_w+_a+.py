'''
r+：读写  写时不能创建文件  文件内容是追加
'''
f = open("alex自述", encoding="utf-8", mode="r+")
content = f.read()
print(content)
f.write("安能物流聚创yysd")
f.close()

'''
w+ 打开一个文件用于读写。
如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件
'''
f = open("alex自述", encoding="utf-8", mode="w+")
content = f.read()
print(content)
f.write("安能物流聚创")
f.close()

'''
a+ 打开一个文件用于读写。
如果该文件已存在，文件指针将会放在文件的结尾,文件打开时会是追加模式。
如果该文件不存在，创建新文件用于读写。
'''
f = open("alex自述", encoding="utf-8", mode="a+")
content = f.read()
print(content)
f.write("安能物流聚创")
f.close()