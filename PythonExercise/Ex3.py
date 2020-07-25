def Calc():
    while True:
        num = int(input('Input Number: '))
        if num > 0 :
            print('> 0')
        elif num < 0:
            print('< 0')
        else:
            print('= 0')
Calc()