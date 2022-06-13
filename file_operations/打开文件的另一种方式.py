"""
Python打开文件的另一种方式：with open() as .... 的形式，这种形式有什么优点?
1)不用手动关闭文件句柄
2)一个with 语句可以操作多个文件，产生多个文件句柄
"""
with open('alex自述', encoding='utf-8') as f1,\
        open('alex自述', encoding='utf-8', mode='w') as f2:
   print(f1.read())
   f2.write("测试思路")
