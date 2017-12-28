import sys

#vscode中运行和python module_using_sys.py we are arguments 比较区别
print('The command line arguments are:')
for i in sys.argv:
    print(i)
print('\n\nThe PYTHONPATH is', sys.path, '\n')

import os; print(os.getcwd())