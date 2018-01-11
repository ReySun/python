class Person:
    # self类始于javascript中的this
    def say_hi(self):
        print('Hello, how are you?', Person.static, Person.__static__, self.static, self.__static__)

    # 没有__开始 或者 __开始且有__结尾的变量，类始于typescript中的static静态变量
    static = 'static'
    __static__ = '__static__'

    # __开始且没有__结尾的变量，类始于typescript中的private私有变量
    __private = 'private'
p = Person()
p.say_hi()
print(Person.static)
print(Person.__static__)
print(Person.__private) # type object 'Person' has no attribute '__private'
