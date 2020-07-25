def Money():
    while True:
        baht = -1
        while baht <= 0:
            baht = float(input('Input Your money(Baht): '))
            if baht <= 0:
                print('You don\'t have Money!')
        dollar = baht /32.8
        profit = dollar*0.3
        print(f'Money Exchange: {dollar:.2f} Dollar')
        print(f'Profit: {profit:.2f}')

Money()
