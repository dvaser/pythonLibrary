import mysql.connector

class DataBase:
    def __init__(self):
        pass

    def connectDB(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1903_bjkDGKN",
            database="schooldb"
        )
        return connection

    def insertStudent(self, no, name, surname, birthdate, gender):
        connection = self.connectDB()

        cursor = connection.cursor()

        sql = "INSERT INTO student(no, name, surname, birthdate, gender) VALUES (%s, %s, %s, %s, %s)"
        values = (no, name, surname, birthdate, gender)

        cursor.execute(sql, values)

        try:
            connection.commit()
            print(f"{cursor.rowcount} adet kayit eklendi.")
        except mysql.connector.errors as err:
            print("ERROR: ", err)
        finally:
            connection.close()

    def insertStudents(self, list):
        connection = self.connectDB()

        cursor = connection.cursor()

        sql = f"INSERT INTO student(no, name, surname, birthdate, gender) VALUES (%s, %s, %s, %s, %s)"
        values = list

        cursor.executemany(sql, values)

        try:
            connection.commit()
            print(f"{cursor.rowcount} adet kayit eklendi.")
        except mysql.connector.errors as err:
            print("ERROR: ", err)
        finally:
            connection.close()

    def getStudents(self):
        connection = self.connectDB()

        cursor = connection.cursor()

        sql = "SELECT * FROM Student"

        cursor.execute(sql)
        result = cursor.fetchall()

        try:
            for i in result:
                print(f"{i[1]} nolu {i[2]} {i[3]} ({i[5]}) adli ogrenci - [{i[4]}]")
        except mysql.connector.errors as err:
            print("ERROR: ", err)
        finally:
            connection.close()

    def getStudentGenderBy(self, gender):
        connection = self.connectDB()

        cursor = connection.cursor()

        sql = f"SELECT * FROM Student WHERE gender='{gender}'"

        cursor.execute(sql)
        result = cursor.fetchall()

        try:
            for i in result:
                print(f"{i[1]} nolu {i[2]} {i[3]} ({i[5]}) adli ogrenci - [{i[4]}]")
        except mysql.connector.errors as err:
            print("ERROR: ", err)
        finally:
            connection.close()

    def getStudentSearch(self, search):
        connection = self.connectDB()

        cursor = connection.cursor()

        sql = f"SELECT * FROM Student WHERE name LIKE '%{search}%' or surname LIKE '%{search}%'"

        cursor.execute(sql)
        result = cursor.fetchall()

        try:
            for i in result:
                print(f"{i[1]} nolu {i[2]} {i[3]} ({i[5]}) adli ogrenci - [{i[4]}]")
        except mysql.connector.errors as err:
            print("ERROR: ", err)
        finally:
            connection.close()

    def updateStudent(self, check, change, no):
        connection = db.connectDB()

        cursor = connection.cursor()

        if check == '1':
            sql = f"UPDATE student SET name='{change}' where no={no}"
        elif check == '2':
            sql = f"UPDATE student SET surname='{change}' where no={no}"
        elif check == '3':
            sql = f"UPDATE student SET birthdate='{change}' where no={no}"
        elif check == '4':
            sql = f"UPDATE student SET gender='{change}' where no={no}"
        else:
            sql = "UPDATE student SET id=1 where id=1"

        cursor.execute(sql)

        try:
            connection.commit()
            print(f"{cursor.rowcount} adet kayit degisti.")
        except mysql.connector.Error as err:
            print("Hata: ", err)
        finally:
            connection.close()

    def deleteStudent(self, no):
        connection = db.connectDB()

        cursor = connection.cursor()

        sql = f"DELETE FROM student WHERE no={no}"

        cursor.execute(sql)

        try:
            connection.commit()
            print(f"{cursor.rowcount} adet kayit silindi.")
        except mysql.connector.Error as err:
            print("Hata: ", err)
        finally:
            connection.close()

db = DataBase()

while True:
    choose = input("\n"+("-"*50)+"""
    \nSorgu ekleme icin\t\t\t\t1
    \rTum sorgulari goruntulemek icin\t\t\t2
    \rCinsiyete gore sorgulari goruntulemek icin\t3
    \rSearch etmek icin\t\t\t\t4
    \rUpdate etmek icin\t\t\t\t5
    \rDelete etmek icin\t\t\t\t6
    \nTuslayiniz:\t""")

    print(("-"*50)+"\n")
    if choose == '1':
        list = []
        count = 0
        while True:
            no = input("No: ")
            name = input("Name: ")
            surname = input("Surname: ")
            birthdate = input("Birthdate: ")
            gender = input("Gender: ")

            list.append((no, name, surname, birthdate, gender))
            count += 1

            result = input("Devam mi? (e/h): ")
            print('-'*50)
            
            if result == 'h':
                print("Kayitlar yukleniyor...")
                break
        if count == 1:
            db.insertStudent(no=no, name=name, surname=surname, birthdate=birthdate, gender=gender)
        else:
            db.insertStudents(list)

    elif choose == '2':
        db.getStudents()

    elif choose == '3':
        gender = input("(E/K): ").upper()
        print("\n"+("-"*50))
        db.getStudentGenderBy(gender)

    elif choose == '4':
        search = input("Aranan ifade: ")
        print("\n"+("-"*50))
        db.getStudentSearch(search)

    elif choose == '5':
        no = input("Ogrenci no:\t")
        check = input("""`
        \r1 - name degis
        \r2 - surname degis
        \r3 - birthdate degis
        \r4 - gender degis
        \r\nDegisecek ifade no:\t""")
        change = input("Yeni ifade:\t")
        
        print(("-"*50)+"\n")
        db.updateStudent(check, change, no)

    elif choose == '6':
        no = input("Ogrenci no:\t")
        print(("-"*50)+"\n")
        db.deleteStudent(no)

