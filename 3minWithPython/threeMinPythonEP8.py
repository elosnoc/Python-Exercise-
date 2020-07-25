
def Thai5000Baht(work):
    if work == 'Programmer':
        print('Not Receive')
    elif work =='Framer':
        print('Not Receive Coz you are framer')
    else:
        print('Wait')

Thai5000Baht('Framer')

#แบบที่ 2
def Thai5000Baht2(work):
    allwork = ['Pro','Farm']
    if work in allwork: #ถ้าค่าที่รับตรงกับใน allwork
        print('Receive')
    else:
        print('wait')

Thai5000Baht2('Framer')