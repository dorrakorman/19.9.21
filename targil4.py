#4. input a number from the user
#     check if the number ahadot and asarot digit are equal and they are (both) above 1
#     you MUST use 1 if (+and)

a = int(input('check number ahadot and asarot digit ='))
b = a // 10  # asarot
c = a % 10  # ahadot

if b == c and b > 1 and c > 1:
    print('ahadot and asarot digit are equal')
else:
    print('ahadot and asarot digit are not equal')