def ChkNumber():
    while True:
        number = -1
        while number < 0:
            number = float(input('Input Number: '))
            if number < 0:
                print('Please insert the number greater or equal zero ')
        if(number >= 50):
            print('Pass')
        else:
            print('Fail')
ChkNumber()