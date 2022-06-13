"""
tell()：使用tell()可以帮我们获取当前光标的位置，单位字节。
"""
f = open("alex自述", encoding="UTF-8")
print(f.tell())
content = f.read()
print(f.tell())
f.close()

"""
seek(n):光标移动到n位置,
注意: 移动单位是byte,所有如果是utf-8的中文部分要是3的倍数，
通常我们使用seek都是移动到开头或者结尾
移动到开头:seek(0)
移动到结尾:seek(0,2) seek的第二个参数表示的是从哪个位置进行偏移,默认是0表示开头,1表示当前位置,2表示结尾
                   seek的第一个参数表示的是偏移量
"""
f = open("alex自述", encoding="utf-8")
f.seek(8,0)
content = f.read()
print(content)
f.close()

"""
flush 强制保存
"""
f = open("文件的其他功能",encoding="utf-8",mode="w")
f.write("fdsgththdj456")
f.flush()
f.close()
