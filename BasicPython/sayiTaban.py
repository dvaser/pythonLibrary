
num = 1

while(num != 0):

    num = int(input("\nSayi giriniz: ")) 

    choose = input("Islem seciniz (1/2): ")

    def ikilikTaban(num):
        def ikilikSistem(num):
            ondalikTaban = 0
            num = str(num)
            sayi = num[::-1]
            for i in range(len(sayi)):
                ondalikTaban += int(sayi[i])*(2**i)
            return ondalikTaban

        print(ikilikSistem(num))

    def sayiTaban(num):
        def sayiSistemi(num, numStyle):
            sayi = ""
            while(num/numStyle != 0):
                kalan = int(num%numStyle)
                num = int(num/numStyle)
                if(kalan<10):
                    sayi += str(kalan)
                else:
                    if(kalan == 10):
                        sayi += 'A'
                    elif (kalan == 11):
                        sayi += 'B'
                    elif (kalan == 12):
                        sayi += 'C'
                    elif (kalan == 13):
                        sayi += 'D'
                    elif (kalan == 14):
                        sayi += 'E'
                    elif (kalan == 15):
                        sayi += 'F'
            return sayi[::-1]

        print(sayiSistemi(num, 2))
        print(sayiSistemi(num, 8))
        print(sayiSistemi(num, 10))
        print(sayiSistemi(num, 16))



    if choose == "1":
        sayi=str(num)
        isBool = True
        for i in sayi:
            if((i != '1') or (i != '0')):
                isBool = False
        if(isBool):    
            ikilikTaban(num)
        else:
            print("Girilen sayi icin yanlis secim.\nIslem seciniz(1/2): 2")
            sayiTaban(num)
    
    
    elif choose == "2":
        sayiTaban(num)
    else:
        print("Hatali sistem sectiniz...")
