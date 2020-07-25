def Temp():
    while True:
        f = -1
        while f < 32:
            f = float(input('Input Fahrenheit: '))
            if f < 32:
                print('Too cold to live')

        Celsius = ((f-32)*5)/9
        print(f'Temp: {Celsius:.2f} Celsius')

Temp()
