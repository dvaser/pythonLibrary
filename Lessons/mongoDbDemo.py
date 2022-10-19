import pymongo
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://dvase:1903_bjkDGKN@cluster0.dhi6emm.mongodb.net/")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# print(myclient.list_database_names())   #? Database adlari sirlanir
# print(mydb.list_collection_names())   #? Collection adlari sirlanir

#! INSERT METHOD

# product = {
#     "name":"Samsung S5",
#     "price":2000
# }

# result = mycollection.insert_one(product)   #? Collectiona urun ekleme fonksiyonu
# print(result.inserted_id)  #? Urunun id numarasi (otomatik verilir)

# productList = [
#     {"name": "Samsung S6","price":3000},
#     {"name": "Samsung S7","price":4000},
#     {"name": "Samsung S8","price":5000},
#     {"name": "Samsung S9","price":6000},
#     {"name": "Samsung S10","price":7000},
#     {"name": "Samsung S11","price":8000}
# ]

# productList = [
#     {"name": "Iphone 13+","price":15450, "description":"Kullanisli telefon"},
#     {"name": "Xiaomi Mi 10","price":6800, "categories":["Telefon", "Elektronik Cihaz"]}
# ]

# result = mycollection.insert_many(productList)   #? Collectiona urunleri ekleme fonksiyonu
# print(result.inserted_ids) #? Urunleri id numarasi (otomatik verilir)

#! FIND & FILTER METHOD

# result = mycollection.find_one()    #? Buldugu ilk kaydi getirir
# result = mycollection.find()    #? Butun kayitlari liste olarak tutar

# filter = {"name":"Samsung"}     #? Filtreleme islemi yapmamizi saglar
# result = mycollection.find(filter,{"_id":0, "name":1})    #? Butun kayitlari liste olarak tutar - 0 olan parametreler gosterilmez 

# for i in result:
#     print(i)    #? Dictionary olarak ekrana gelir

# result = mycollection.find_one({"_id":"634c296dbf96b0684861f0a7"}) #? Bu boyle calismaz cunku id ObjectId olmali
# result = mycollection.find_one({"_id": ObjectId("634c296dbf96b0684861f0a7")}) #? Bu boyle calismaz cunku id ObjectId olmali

# result = mycollection.find({  #* MongoDb Operation Query
#     "name": {
#         # "$in" : ["Samsung S5", "Samsung S6"]    #? Bunlardan birini icerirse (in) getirir
#         "$regex" : "^S"    #? regex - (Reguler Exprestion) fonksiyonlari icerir
#     }
# })

# result = mycollection.find({    #* MongoDb Operation Query
#     "price": {
#         # "$gt" : 2000    #? gt (greater than) - 2000'den buyuk olan
#         # "$gte" : 2000    #? gte  (greater than equie) - 2000'den buyuk ve esit olan
#         # "$eq" : 2000    #? eq (equie) - 2000 esit olan
#         # "$lte" : 2000    #? lte (last thane equie) - 2000'den kucuk ve esit olan
#         "$lt" : 2000    #? lt (last than) - 2000'den kucuk olan
#     }
# })

#! SORT METHOD

# result = mycollection.find().sort("name", 1)    #? Artan sekilde siralanir
# result = mycollection.find().sort("price", -1)  #? Azalan sekilde siralanir
# result = mycollection.find().sort([("name", 1),("price", -1)])  #? Coklu siralama

# for i in result:
#     print(i)

#! UPDATE METHOD

# mycollection.update_one(    #? Birden fazla benzer kayit varsa gelen ilk kayit yenilenir
#     {"name":"Samsung S6"},    #* query
#     {"&set":{
#         "name":"Iphone 12",
#         "price":11700
#     }}
# )

# mycollection.update_many(    #? Birden fazla benzer kayit varsa gelen tum kayitlari yenilenir
#     {"name":"Samsung S6"},    #* query
#     {"&set":{
#         "name":"Iphone 12",
#         "price":11700
#     }}
# )

# print(result.modified_count)   #? Kayit guncellenme adet

#! DELETE METHOD

# result = mycollection.delete_one({"name":"Samsung S7"}) #? Belirlenen kaydi siler
# result = mycollection.delete_many({"name":{"$regex":"^S"}}) #? Belirlenen kayitlari siler

# result.deleted_count    #? Silinen kayitlarin adeti