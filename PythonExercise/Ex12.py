def EvenOdd():
    while True:
        num = int(input('Input number: '))
        if num == 0:
            print('Zero')
        elif num < 0:
            if num % 2 == 0:
                print('Negative Even')
            else:
                print('Negative Odd')
        else:
            if num % 2 == 0:
                print('Positive Even')
            else:
                print('Positive Odd')
EvenOdd()