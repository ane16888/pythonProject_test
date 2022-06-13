"""
文件操作的改的步骤：
1)以读的模式打开原文件
2)以写的模式创建一个新文件
3)将原文件的内容读出来修改成新内容，写入新文件
4)将原文件删除
5)将新文件重命名成原文件
"""
import os
with open("alex自述",encoding="utf-8") as f1,open("alex自述.back", encoding="utf-8", mode="w") as f2:
    for line in f1:
        new_line = line.replace("alex","SB")
        f2.write(new_line)
os.remove("alex自述")
os.rename("alex自述.back", "alex自述")