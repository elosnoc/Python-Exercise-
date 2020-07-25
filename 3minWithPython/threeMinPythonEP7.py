def Calc(qty,price):
    return qty * price

def Run():
    while True:
        q = int(input('Input Qty: '))
        p = int(input('Input Price: '))
        result = Calc(q,p)
        print(f'Total is => {result:.2f} Baht')
        print('---------------------------')
Run()