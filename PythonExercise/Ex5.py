def Chk():
    while True:
        char = input('Input Character: ')
        if char =='A':
            print('[80,100]')
        elif char =='B':
            print('[70,80]')
        elif char =='C':
            print('[60,70]')
        elif char =='D':
            print('[50,60]')
        elif char =='F':
            print('[0,50]')
        else:
            print('Error')
Chk()