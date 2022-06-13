# 打开方式：读、写、追加、读写、写读....
# 编码方式：utf-8、gbk、gb2312......
f = open("alex自述", encoding="utf-8", mode="r")
content = f.read()
print(content)
f.close()
'''
open： 内置函数，open底层调用的是操作系统的接口。
f：变量，f,fh,file_handler,f_h 文件句柄。对文件进行的任何操作都是通过文件句柄。
encoding：可以不写，不写参数，默认编码本：
windows：gbk   linux：utf-8   mac：utf-8
f1.close() 关闭文件句柄
'''
'''
文件操作三部曲
1.打开文件，得到文件句柄并赋值给一个变量
2.通过句柄对文件进行操作
3.关闭文件
'''
'''
报错原因
1)UnicodeDecodeError:
文件存储时与文件打开时编码本运用不一致
2)路径分隔符产生的问题：
在路径的整体前面加一个r， 
r'C:\\Users\金鑫\Desktop\\111.txt'
'''
