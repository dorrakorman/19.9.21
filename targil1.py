# 1. input a number check if it is divided by 10 without reminder
#      you need to check if it is % 5 and % 2 == 0, if so print ('can be divided by 10')

a = int(input('enter number to check: a = '))

if (a % 5 == 0) and (a % 2 == 0):
    print('can be divided by 10')
else:
    # print('can\'t be divided by 10')  # possible solution to ignore symbol '
    print("can't be divided by 10")
