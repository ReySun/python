def say_hello():
    # 该块属于这一函数
    print('hello world')
    return 'return' ## 默认None
say_hello()  # 调用函数
say_hello()  # 再次调用函数
print(say_hello())


# 函数参数
def print_max1(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')
print_max1(3, 4)


# 局部变量
x = 50
def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)
func(x)
print('x is still', x)


# global 语句
x = 50
def func1():
    global x

    print('x is', x)
    x = 2
    print('Changed global x to', x)
func1()
print('Value of x is', x)


# 默认参数值 末尾的参数才能被赋予默认参数值
def say(message, times=1):
    print(message * times)
say('Hello')
say('World', 5)


# 关键字参数
def func2(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)
func2(3, 7)
func2(25, c=24)
func2(c=50, a=100)


# 可变参数
def total(a=5, *numbers, **phonebook):
    ''' 当我们声明一个诸如 *param 的星号参数时，从此处开始直到结束的所有位置参数（Positional Arguments）都将被收集并汇集成一个称为“param”的元组（Tuple）。
    类似地，当我们声明一个诸如 **param 的双星号参数时，
    从此处开始直至结束的所有关键字参数都将被收集并汇集成一个名为 param 的字典（Dictionary）。 '''
    print('a', a)
    #遍历元组中的所有项目
    for single_item in numbers:
        print('single_item', single_item)
    #遍历字典中的所有项目
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)
print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))


# DocStrings
''' 该文档字符串所约定的是一串多行字符串，其中第一行以某一大写字母开始，以句号结束。

    第二行为空行，
    后跟的第三行开始是任何详细的解释说明。5在此强烈建议你在你所有重要功能的所有文档字符串中都遵循这一约定。 '''
def print_max2(x, y):
    '''Prints the maximum of two numbers.打印两个数值中的最大数。

    The two values must be integers.这两个数都应该是整数'''
    # 如果可能，将其转换至整数类型
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max2(3, 5)
print(print_max2.__doc__)