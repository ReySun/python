# from..import 语句
from mymodule import say_hi, __version__

say_hi()
print('Version', __version__)

# from mymodule import *
''' 这将导入诸如 say_hi 等所有公共名称，但不会导入 __version__ 名称，因为后者以双下划线开头。

警告：要记住你应该避免使用 import-star 这种形式，即 from mymodule import *。 '''