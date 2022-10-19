import random 

num = random.randint(0,100)


def func(result):
    if result == 'b':
        result = 'buyuk'.title()
    elif result == 's':
        result = 'kucuk'.title()
    elif result == '=':
        result = 'dogru'.title()

    return f"{result} bir sayi girdiniz"

guessNum = int(input("Guess Num: "))
while num != guessNum:
    if num > guessNum:
        print(func(result='s'))
    elif num < guessNum:
        print(func(result='b'))

    guessNum = int(input("Guess Num: "))
else:
    print(func(result='='))