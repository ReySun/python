# encoding=utf-8
import io
import os

target_dir = 'data'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # 创建目录
target_file = target_dir + '/abc.txt'

f = io.open(target_file, "wt", encoding="utf-8")
f.write(u"Imagine non-English language here")
f.close()

text = io.open(target_file, encoding="utf-8").read()
print(text)