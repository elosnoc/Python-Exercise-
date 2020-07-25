def chistYear():
    while True:
        year = -1
        while year < 0:
            year = int(input('Input BC Year: '))
            if year < 0:
                print('Input more zero')

        BuddhistEra = year + 543
        print(f'Buddhist Era is: {BuddhistEra}')

chistYear()


