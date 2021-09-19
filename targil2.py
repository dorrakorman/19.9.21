#2. input a number. check if the number is 0 or 1, if so print '0 or 1
#    otherwise check if the number is -1, if so print '-1'
#   otherwise print 'unknown number'

a = int(input('input num to check a = '))
if a == 0 or a == 1:
    print('num is 0 or 1')
else:
    if a == -1:
        print('num is -1')
    else:
#         if a < -1 or a > 1:
        print('unknown num')