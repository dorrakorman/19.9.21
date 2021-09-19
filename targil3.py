#3. input a number from the user
#     check if the number has 2 digits, if so print the ahadot digit
#     you MUST use 1 if (+and)

a = int(input('check 2 digits number ='))
if a // 10 and a % 10:
    print(a % 10)
else:
    print('wrong number')