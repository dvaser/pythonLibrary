from math import factorial

def minNum(*args):
    num = min(args)
    return num, factorial(num)

num, fac = minNum(5,4,8,27,6,9)

print(f"En kucuk sayi : {num}\nBu sayinin faktoriyeli: {fac}")