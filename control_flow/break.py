# break 和javascript中的行为一致(退出此次循环语句)
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')