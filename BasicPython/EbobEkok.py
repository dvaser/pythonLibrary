a = 75
b = 45
ek = a*b
eb = 0

while (a and b):
    if (b > a):
        b -= a
    else:
        a -= b

if (a):
    eb = a
else:
    eb = b

print(f"Ebob: ", eb)
print("Ekok: ", ek/eb)