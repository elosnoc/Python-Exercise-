def ChkVowel(x='x'):
    vowel = ['a','e','i','o','u']
    if x in vowel:
        print('There is Vowel')
    else:
        print('There is not Vowel')


while True:
    ChkVowel(input('Enter Charater: '))