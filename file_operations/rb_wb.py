'''
rb模式：以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。
主要是操作非文字文件：图片，音频，视频等,并且带有b的模式操作文件，不用声明编码方式
rb模式有read read(n) readline(),readlines() for循环等方法。
'''''
f = open(r"C:\\Users\DELL\Desktop\\地址和模板匹配.png",mode="rb")
content = f.read()
print(content)
f.close()

'''
Wb模式  以二进制写模式打开
'''''
f = open(r"C:\\Users\DELL\Desktop\\地址和模板匹配.png",mode="rb")
content = f.read()
f.close()
f1 = open(r"C:\\Users\DELL\Desktop\\地址和模板匹配复制.png",mode="wb")
f1.write(content)
f1.close()


