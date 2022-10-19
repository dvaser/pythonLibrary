import json
import os

filePath = "users.json"

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}   #? bos <dict> tanimlamasi

        #! Load users from .json file
        self.loadUsers()

    def loadUsers(self):    #? Dosyadaki tum bilgiyi Class olarak self.users icine kayit ediyoruz (Uyg acilir acilmaz etkin)
        if os.path.exists(filePath):
            with open(filePath, "r", encoding="utf-8") as file:
                users = json.load(file)
                
                for user in users:
                    user = json.loads(user)
                    newUser = User(username=user["username"], password=user["password"], email=user["email"])
                    self.users.append(newUser)

    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print("Kullanici olusturuldu..")

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user     #? user <dict> tanimlamasi
                print("Giris yapildi...")
                break

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}   #? bos <dict> tanimlamasi
        print("Cikis yapildi...")

    def identity(self):
        if self.isLoggedIn:
            print(f"username: {self.currentUser.username}")
        else:
            print("Giris yapilmadi.")

    def savetoFile(self):   #? self.users icindeki tum bilgiyi dosya icine dict olarak kayit ediyoruz (Register zamani etkin)
        list = []

        for user in self.users:                     #? self.users icindeki class yapisi oldugu icin kayit edemem
            list.append(json.dumps(user.__dict__))  #? user, self.users icindeki class'lar ve __dict__ ile her biri dict olur

        with open(filePath, "w") as file:   #? .json dosyamiza User() elemanlarimizi dict olarak yazdiriyoruz
            json.dump(list, file)     


repository = UserRepository()



while True: 
    print("Menu".center(50,'*'))
    secim = int(input("1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\n\nSeciniz: "))
    if secim == 5:
        break
    else:
        if secim == 1:    #! Register
            username = input("Username: ")
            password = input("Password: ")
            email = input("E-mail: ")

            user = User(username=username, password=password, email=email)
            repository.register(user)

        elif secim == 2:    #! Login
            if repository.isLoggedIn:
                print("Zaten giris yapili")
            else:
                username = input("Username: ")
                password = input("Password: ")

                repository.login(username=username, password=password)
        
        elif secim == 3:    #! Logout
            repository.logout()
            
        elif secim == 4:    #! Identity
            repository.identity() 
        else:
            print("Yanlis secim...")