import random

def love_calculator(person1, person2, score):
    love = random.randint(0,100) + score
    return love

person1 = input("Birinci kisinin adi: ")
person2 = input("Ikinci kisinin adi: ")

length_diff = abs(len(person1) - len(person2))

the_same_letters = 0

for letter in person1:
    if letter in person2:
        the_same_letters += 1

score = the_same_letters - length_diff

love_score = love_calculator(person1=person1, person2=person2, score=score)

print(str(love_score) + "%")