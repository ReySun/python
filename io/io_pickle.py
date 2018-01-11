''' Python 提供了一个叫作 Pickle 的标准模块，通过它你可以将任何纯 Python 对象存储到一个文件中，并在稍后将其取回。这叫作持久地（Persistently）存储对象 '''
import pickle
import os

target_dir = 'data'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # 创建目录


# 我们存储相关对象的文件的名称
shoplistfile = target_dir + '/shoplist.data'

# 需要购买的物品清单
shoplist = ['apple', 'mango', 'carrot']

# 准备写入文件
f = open(shoplistfile, 'wb') # 通过 open 以写入（write）二进制（binary）
# 转储对象至文件
pickle.dump(shoplist, f)
f.close()

# 清除 shoplist 变量
del shoplist

# 重新打开存储文件
f = open(shoplistfile, 'rb')
# 从文件中载入对象
storedlist = pickle.load(f) # 通过 pickle 模块的 load 函数接收返回的对象
print(storedlist)