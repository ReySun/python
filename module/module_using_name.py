# 模块的 __name__
''' 类始于nodeJS的 require.main === module '''

if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')