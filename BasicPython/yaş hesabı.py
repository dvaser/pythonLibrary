def myAge():
    print()
    print("Doğum Tarihin")
    print()
    global day, month, year, age
    day= int(input("Gün: "))
    month= int(input("Ay: "))
    year= int(input("Yıl: "))
    print()
    age= "Doğum Tarihin: " + str(day) + "/" + str(month) + "/" + str(year) 
    print(age)
    print()
    print()   
    print("Bugünün Tarihi")
    print()
    global day2, month2, year2, time
    day2= int(input("Gün: "))
    month2= int(input("Ay: "))
    year2= int(input("Yıl: "))
    print()
    time= "Bugünün Tarihi: " + str(day2) + "/" + str(month2) + "/" + str(year2)
    print(time)
    
    global day1, month1, year1, age1
    if day>day2:
        day1= 30+day2-day
        if month>month2:
            month1= 12+month2-1-month
            year1= year2-1-year
        elif month2>month:
            month1= month2-1-month
            year1= year2-year
    
    elif day2>day:
        day1= day2-day
        if month>month2:
            month1= 12+month2-month
            year1= year2-1-year
        elif month2>month:
            month1= month2-month
            year1= year2-year
    age1= "Yaşama Süren: " + str(day1) + " gün/" + str(month1) + " ay/" + str(year1) + " yıl"
    print()
    print()
    print()
    print(age1)
    print()
    print(age)
    print()
    print(time)
    print()
    print("Yaşama Süren (Gün): "+ str(int(day1 + (month1*30) + (year1*12*30))))
    print()
    print()
    

# Doğum Tarihim çıktı
# Bugünün Tarihi çıktı
# Yaşama Sürem çıktı 

def islem():
    global choose
    choose=int(input("İşlemi giriniz: "))

while True:
    print("Başlamak/Başa dönmek için 0'ı tuşlayınız.")
    islem()
    if choose == 0:
        myAge()
    elif choose == 1:
        pass