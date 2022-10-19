"""
    ! Dogukan Vatansever
    ? Game
    * 
    todo:
    FIXME
"""


import random

wellcome = "Oyunumuza hoş geldin!!"
wellcome = wellcome.center(50,'-')
print("\n"+"-"*(len(wellcome))+"\n"+wellcome+"\n"+"-"*(len(wellcome))+"\n")

numberOfUser = int(input("Oyunu kaç kişi oynayacak? : "))
print(" \n"+("-"*50))
if type(numberOfUser) is not int:
    print("\n DİKKAT !!\n\n Hatalı karakter girdiniz. Tekrar deneyiniz.\n")
    numberOfUser = int(input("Oyunu kaç kişi oynayacak? : "))
    print("\n"+("-"*50))

def cls():
    print('\n'*100)
print()
user = []
j = 0
i = 0
remainingHeart = 10
for x in range(numberOfUser):
    j+=1
    userName = input(f"    {j}.Kullanıcının Adı:       ").title()
    userSurname = input(f"    {j}.Kullanıcının Soyadı:    ").title()
    userAge = input(f"    {j}.Kullanıcının Yaşı:      ")
    userGender = input(f"    {j}.Kullanıcının Cinsiyeti: ").title()
    print("\n"+"-"*50)
    if (type(userName or userSurname or userGender) is not str) or (type(int(userAge)) is not int):
        print("\n DİKKAT !!\n\n Hatalı karakter girdiniz. Tekrar deneyiniz.\n")
        userName = input(f"    {j}.Kullanıcının Adı:       ").title()
        userSurname = input(f"    {j}.Kullanıcının Soyadı:    ").title()
        userAge = input(f"    {j}.Kullanıcının Yaşı:      ")
        userGender = input(f"    {j}.Kullanıcının Cinsiyeti: ").title()
    else:
        i+=1
        user.append(
            {
                'userName': userName, 
                'userSurname': userSurname, 
                'userAge': userAge, 
                'userGender': userGender,
                'userId': i,
                'userHeart': remainingHeart,
                'userScore': 50
            }
        )
        print(f"\nTebrikler, {j}.kullanıcı girişiniz başarılı.\n\n"+("-"*50)+"\n")
input("İlerlemek için tuşlayınız: ")
cls()   
print("\n\nOyun başlıyor . . .\n\n"+("*"*50))
print("\nOYUNUN KURALLARI"+"\n"+("^"*16)+"\n\n1) Her kullanıcının 10 adet can hakkı vardır."+"\n\n2) Her kullanıcıya verilen başlangıç puanı 50'dir."+"\n\n3) Rastgele oluşturulmuş 0 ile 100 arasındaki sayı, kullanıcılar tarafından bulunmaya çalışılır."+"\n\n4) Puanlamada; -1 azalma sayının (-5/+5)"+"\n               -2 azalma sayının (-10/+10)"+"\n               -4 azalma sayının (-20/+20)"+"\n               -7 azalma sayının (-35/+35)"+"\n               -10 azalma sayının (-50/+50)    aralığında olduğunu gösterir."+"\n\n"+("*"*50))    
input("\nSayının oluşması için tuşlayınız: ")
number = random.randint(1,100)
print("\n"+("-"*50))
print()
print(f"Bulmanız gereken sayınız oluşturuldu. {numberOfUser} kullanıcıya da başarılar.")
print()
input("İlerlemek için tuşlayınız: ")
cls() 

print("\n"+("-"*50)+"\n")
for x in range(numberOfUser):
    print(f"{user[x]['userName']} {user[x]['userSurname']} kalan canın: {user[x]['userHeart']}\n")
print(("-"*50))

print()

guessNum = 0
for hearts in range(remainingHeart):
    for gamer in range(numberOfUser):
        print(("="*50)+"\n")
        guessNum = int(input(f"{user[gamer]['userName']} {user[gamer]['userSurname']}, sence sayı kaçtır? : "))
        if guessNum == number:
            print("\n"+("*"*50)+"\n")
            user[gamer]['userHeart'] = user[gamer]['userHeart']-1
            print(f"{user[gamer]['userName']} {user[gamer]['userSurname']}, oyunu kazandın.")
            print("\n"+("*"*50)+"\n")
            for x in range(numberOfUser):
                print(f"{user[x]['userName']} {user[x]['userSurname']}\nKalan canın: {user[x]['userHeart']}\nPuanın: {user[x]['userScore']}\n")
            exit = input("---------------------------------\nOyundan çıkmak için tuşlatınız: ")
            while exit is str():
                break
        elif guessNum in range(number-99,number+99):
            if guessNum in range(number-50,number+50):
                if guessNum in range(number-35,number+35):
                    if guessNum in range(number-20,number+20):
                        if guessNum in range(number-10,number+10):
                            if guessNum in range(number-5,number+5):
                                if number-5 <= guessNum < number:
                                    print("\nSayının aşağı değerlerindesin.")
                                    user[gamer]['userHeart'] = user[gamer]['userHeart']-1
                                    print(f"\n{user[gamer]['userName']} {user[gamer]['userSurname']} kalan canın: {user[gamer]['userHeart']}")
                                    print(f"\nPuanın: {user[gamer]['userScore']} iken {user[gamer]['userScore']-1} oldu\n")
                                    user[gamer]['userScore'] = user[gamer]['userScore']-1     
                                elif number < guessNum <= number+5:
                                    print("\nSayının yukarı değerlerindesin.")    
                                    user[gamer]['userHeart'] = user[gamer]['userHeart']-1
                                    print(f"\n{user[gamer]['userName']} {user[gamer]['userSurname']} kalan canın: {user[gamer]['userHeart']}")
                                    print(f"\nPuanın: {user[gamer]['userScore']} iken {user[gamer]['userScore']-1} oldu\n")
                                    user[gamer]['userScore'] = user[gamer]['userScore']-1             
                            else:
                                if number-10 <= guessNum < number-5:
                                    print("\nSayının aşağı değerlerindesin.")
                                    user[gamer]['userHeart'] = user[gamer]['userHeart']-1
                                    print(f"\n{user[gamer]['userName']} {user[gamer]['userSurname']} kalan canın: {user[gamer]['userHeart']}")
                                    print(f"\nPuanın: {user[gamer]['userScore']} iken {user[gamer]['userScore']-2} oldu\n")
                                    user[gamer]['userScore'] = user[gamer]['userScore']-2                                        
                                elif number+5 < guessNum <= number+10:
                                    print("\nSayının yukarı değerlerindesin.")    
                                    user[gamer]['userHeart'] = user[gamer]['userHeart']-1
                                    print(f"\n{user[gamer]['userName']} {user[gamer]['userSurname']} kalan canın: {user[gamer]['userHeart']}")
                                    print(f"\nPuanın: {user[gamer]['userScore']} iken {user[gamer]['userScore']-2} oldu\n")
                                    user[gamer]['userScore'] = user[gamer]['userScore']-2                                      
                        else:
                            if number-20 <= guessNum < number-10:
                                print("\nSayının aşağı değerlerindesin.")
                                user[gamer]['userHeart'] = user[gamer]['userHeart']-1
                                print(f"\n{user[gamer]['userName']} {user[gamer]['userSurname']} kalan canın: {user[gamer]['userHeart']}")
                                print(f"\nPuanın: {user[gamer]['userScore']} iken {user[gamer]['userScore']-4} oldu\n")
                                user[gamer]['userScore'] = user[gamer]['userScore']-4                               
                            elif number+10 < guessNum <= number+20:
                                print("\nSayının yukarı değerlerindesin.")    
                                user[gamer]['userHeart'] = user[gamer]['userHeart']-1
                                print(f"\n{user[gamer]['userName']} {user[gamer]['userSurname']} kalan canın: {user[gamer]['userHeart']}")
                                print(f"\nPuanın: {user[gamer]['userScore']} iken {user[gamer]['userScore']-4} oldu\n")
                                user[gamer]['userScore'] = user[gamer]['userScore']-4                                 
                    else:
                        if number-35 <= guessNum < number-20:
                            print("\nSayının aşağı değerlerindesin.")
                            user[gamer]['userHeart'] = user[gamer]['userHeart']-1
                            print(f"\n{user[gamer]['userName']} {user[gamer]['userSurname']} kalan canın: {user[gamer]['userHeart']}")
                            print(f"\nPuanın: {user[gamer]['userScore']} iken {user[gamer]['userScore']-7} oldu\n")
                            user[gamer]['userScore'] = user[gamer]['userScore']-7   
                        elif number+20 < guessNum <= number+35:
                            print("\nSayının yukarı değerlerindesin.")    
                            user[gamer]['userHeart'] = user[gamer]['userHeart']-1
                            print(f"\n{user[gamer]['userName']} {user[gamer]['userSurname']} kalan canın: {user[gamer]['userHeart']}")
                            print(f"\nPuanın: {user[gamer]['userScore']} iken {user[gamer]['userScore']-7} oldu\n")
                            user[gamer]['userScore'] = user[gamer]['userScore']-7                
                else:
                    if number-50 <= guessNum < number-35:
                        print("\nSayının aşağı değerlerindesin.")
                        user[gamer]['userHeart'] = user[gamer]['userHeart']-1
                        print(f"\n{user[gamer]['userName']} {user[gamer]['userSurname']} kalan canın: {user[gamer]['userHeart']}")
                        print(f"\nPuanın: {user[gamer]['userScore']} iken {user[gamer]['userScore']-10} oldu\n")
                        user[gamer]['userScore'] = user[gamer]['userScore']-10     
                    elif number+35 < guessNum <= number+50:
                        print("\nSayının yukarı değerlerindesin.")    
                        user[gamer]['userHeart'] = user[gamer]['userHeart']-1
                        print(f"\n{user[gamer]['userName']} {user[gamer]['userSurname']} kalan canın: {user[gamer]['userHeart']}")
                        print(f"\nPuanın: {user[gamer]['userScore']} iken {user[gamer]['userScore']-10} oldu\n")
                        user[gamer]['userScore'] = user[gamer]['userScore']-10                 
            else:
                if number-99 <= guessNum < number-50:
                    print("\nSayının aşağı değerlerindesin.")
                    user[gamer]['userHeart'] = user[gamer]['userHeart']-1
                    print(f"\n{user[gamer]['userName']} {user[gamer]['userSurname']} kalan canın: {user[gamer]['userHeart']}")
                    print(f"\nPuanın: {user[gamer]['userScore']} iken {user[gamer]['userScore']-20} oldu\n")
                    user[gamer]['userScore'] = user[gamer]['userScore']-20             
                elif number+50 < guessNum <= number+99:
                    print("\nSayının yukarı değerlerindesin.")    
                    user[gamer]['userHeart'] = user[gamer]['userHeart']-1
                    print(f"\n{user[gamer]['userName']} {user[gamer]['userSurname']} kalan canın: {user[gamer]['userHeart']}")
                    print(f"\nPuanın: {user[gamer]['userScore']} iken {user[gamer]['userScore']-20} oldu\n")
                    user[gamer]['userScore'] = user[gamer]['userScore']-20
                

