
def Sales(product,price,qty):
    print(f'Products:{product}')
    print(f'Qty:{qty}')
    calc = price * qty
    print(f'Sum is: {calc} Baht')
    return calc # save value in total 



total = Sales('shoe',1400,10)

total + (total *0.1)