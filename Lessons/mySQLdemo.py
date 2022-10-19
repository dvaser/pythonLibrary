import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1903_bjkDGKN",
    database = "myapp"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE myDatabase")

'''
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
'''

# mycursor.execute("CREATE TABLE customers (name VARCHAR(40), address VARCHAR(255))")


def createDB(databaseName):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1903_bjkDGKN"
    )
    cursor = connection.cursor()

    sql = f"CREATE DATABASE {databaseName}"

    cursor.execute(sql)
    try:
        connection.commit
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close()

def createTable(tableName, *args):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1903_bjkDGKN",
        database = "myapp"
    )
    cursor = connection.cursor()

    sql = f"CREATE TABLE {tableName} ({str(args)})"

    cursor.execute(sql)
    try:
        connection.commit
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close()

'''
mycursor.execute(
    """CREATE TABLE student 
        (id INT NOT NULL AUTO_INCREMENT, 
        no INT,
        name VARCHAR(50), 
        surname VARCHAR(50), 
        birthdate DATE, 
        gender VARCHAR(20), 
        PRIMARY KEY(id))
    """)
'''

def insertProduct(name, price, imageUrl='', description=''):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1903_bjkDGKN",
        database = "myapp"
    )
    cursor = connection.cursor()

    sql = f"INSERT INTO Products(name, price, imageUrl, description) VALUES (%s, %s, %s, %s)"
    values = (name, price, imageUrl, description)

    cursor.execute(sql, values)
    try:
        connection.commit()
        print(f"{cursor.rowcount} adet kayit eklendi.")
        print(f"Son kayit ID: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close()

# insertProduct(name='APPLE', price=12300, imageUrl='', description='')
# insertProduct(name='APPLE', price=11002, imageUrl='', description='')

"""
list = []
while True:
    name = input("Product Name: ")
    price = float(input("Product Price: "))
    imageUrl = input("Product ImageUrl: ")
    description = input("Product Description: ")

    list.append((name, price, imageUrl, description))

    result = input("Devam etmek istiyor musun? (e/h): ")
    print("-"*50)
    
    if result == 'h':
        print("Kayitlar aktariliyor...")
        break
"""


# commit edilmeli
def insertProducts(list):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1903_bjkDGKN",
        database = "myapp"
    )
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name, price, imageUrl, description) VALUES (%s, %s, %s, %s)"
    values = list

    cursor.executemany(sql, values)     # SQL cumlecigi ile degerleri tek seferde execute eder
    try:
        connection.commit()
        print(f"{cursor.rowcount} adet kayit eklendi.")
        print(f"Son kayit ID: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close()


def getProducts():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1903_bjkDGKN",
        database = "myapp"
    )
    cursor = connection.cursor()

    # cursor.execute("SELECT * FROM Products")
    cursor.execute("SELECT name, price FROM Products WHERE id>1 and name='Apple'")
    # cursor.execute("SELECT name, price FROM Products WHERE name LIKE '%App%'")
    # cursor.execute("SELECT name, price FROM Products WHERE name LIKE '%App%' and price>3000")

    result = cursor.fetchall() # Birden fazla kayit almak istedigimizde
    # result = cursor.fetchone() # Bir kayit almak istedigimizde (ilkini)

    for i in result:
        print(f"Name: {i[0]}\tPrice: {i[1]}")

def getProductById(id):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1903_bjkDGKN",
        database = "myapp"
    )
    cursor = connection.cursor()

    sql = "SELECT name, price FROM Products WHERE id=%s"
    params = (id,)

    # cursor.execute("SELECT * FROM Products")
    # cursor.execute("SELECT name, price FROM Products WHERE id>1 and name='Apple'")
    cursor.execute(sql, params)
    # cursor.execute("SELECT name, price FROM Products WHERE name LIKE '%App%'")
    # cursor.execute("SELECT name, price FROM Products WHERE name LIKE '%App%' and price>3000")

    result = cursor.fetchone() # Bir kayit almak istedigimizde (ilkini)

    print(f"Name: {result[0]}\tPrice: {result[1]}")

# getProductById(1)
# getProductById(2)

def getProductOrder(order, by='ASC'):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1903_bjkDGKN",
        database = "myapp"
    )
    cursor = connection.cursor()

    sql = f"SELECT name, price FROM Products ORDER BY {order} {by}"

    cursor.execute(sql)

    result = cursor.fetchall() # Birden fazla kayit almak istedigimizde
    # result = cursor.fetchone() # Bir kayit almak istedigimizde (ilkini)

    for i in result:
        print(f"Name: {i[0]}\tPrice: {i[1]}")

# getProductOrder('name, price', "DESC")

def getProductInfo():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1903_bjkDGKN",
        database = "myapp"
    )
    cursor = connection.cursor()

    # sql = "SELECT COUNT(*) FROM Products"
    # sql = "SELECT AVG(price) FROM Products"
    # sql = "SELECT SUM(price) FROM Products"
    # sql = "SELECT MAX(price) FROM Products"
    # sql = "SELECT MIN(price) FROM Products"
    sql = "SELECT name, price FROM Products WHERE price = (SELECT MIN(price) FROM Products)"

    cursor.execute(sql)

    result = cursor.fetchone() # Bir kayit almak istedigimizde (ilkini)

    print(f"Result: {result[0]} {result[1]}")

# getProductInfo()

def getProductsSearch(search):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1903_bjkDGKN",
        database = "myapp"
    )
    cursor = connection.cursor()

    sql = f"SELECT * FROM Products WHERE name LIKE '%{search}%' or description LIKE '%{search}%'"

    cursor.execute(sql)
    result = cursor.fetchall()

    try:
        for i in result:
            #print(f"{i[1]} nolu {i[2]} {i[3]} ({i[5]}) adli ogrenci - [{i[4]}]")
            print(i)
    except mysql.connector.errors as err:
        print("ERROR: ", err)
    finally:
        connection.close()

"""
while True:
    result = input("Search: ")
    getStudentSearch(result)
"""

#commit edilmeli
def updateProduct(check, change, id):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1903_bjkDGKN',
        database='myapp'
    )

    cursor = connection.cursor()

    sql = f"UPDATE products SET {check}='{change}' where id={id}"

    cursor.execute(sql)

    try:
        connection.commit()
        print(f"{cursor.rowcount} adet kayit degisti.")
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close()

# updateProduct('price', '15000', 8)

def deleteProduct(id):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1903_bjkDGKN',
        database='myapp'
    )

    cursor = connection.cursor()

    sql = f"DELETE FROM products where id={id}"

    cursor.execute(sql)

    try:
        connection.commit()
        print(f"{cursor.rowcount} adet kayit silindi.")
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close()

def getProductsOn():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1903_bjkDGKN",
        database = "myapp"
    )
    cursor = connection.cursor()

    # Tablolari foregein ile birlestirildigi yerden (ON komutu) ekliyoruz (inner join)
    sql = "SELECT p.name, p.price, c.name FROM Products AS p INNER JOIN Categories AS c ON p.Categoryid=c.id"
    cursor.execute(sql)

    result = cursor.fetchall() # Birden fazla kayit almak istedigimizde
    # result = cursor.fetchone() # Bir kayit almak istedigimizde (ilkini)

    for i in result:
        print(i)

getProductsOn()