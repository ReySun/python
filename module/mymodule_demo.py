import mymodule #使用自定义模块，会有__pycache__目录进行缓存

mymodule.say_hi()
print('Version', mymodule.__version__)

# 模块的 __name__
import module_using_name  #单独运行 module_using_name.py 查看区别