def GPA():
    while True:
        score = -1
        while score < 0:
            score = float(input('Input Score: '))
            if score < 0:
                print('Please insert the SCORE greater or equal zero')
        if score >= 80:
            print('A')
        elif score >= 70:
            print('B')
        elif score >= 60:
            print('C')
        elif score >= 50:
            print('D')
        else:
            print('F')
GPA()