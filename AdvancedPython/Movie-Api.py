import requests


class Movie:
    def __init__(self):
        self.api_URL = "https://api.themoviedb.org/3"
        self.api_key = "e8a9d5f82d78ca210c8076d648685c12"
        self.language = "tr-TR"

    def getSearch(self, movie):
        response = requests.get(self.api_URL+"/search/movie?api_key="+self.api_key+"&query="+movie+"&language="+self.language+"&page=1")
        return response.json()

    def getPopular(self):
        response = requests.get(self.api_URL+"/movie/popular?api_key="+self.api_key+"&language="+self.language+"&page=1")
        return response.json()

    def getNow(self):
        response = requests.get(self.api_URL+"/movie/now_playing?api_key="+self.api_key+"&language="+self.language+"&page=1")
        return response.json()

    def getTopRated(self):
        response = requests.get(self.api_URL+"/movie/top_rated?api_key="+self.api_key+"&language="+self.language+"&page=1")
        return response.json()


movie = Movie()

while True:
    ch = int(input("\n1- Film bul\n2- En populer filmler\n3- Vizyondaki filmler\n4- En yuksek puani alan filmler\n5- Cikis\n\nSeciniz: "))
    print("\n")
    if ch == 5:
        break
    else:
        if ch == 1:
            keyword = input("Aradiginiz filmin adi: ")
            print("\n")
            movies = movie.getSearch(movie=keyword)
            for movie in movies['results']:
                print(movie['title'])
        elif ch == 2:
            movies = movie.getPopular()
            for movie in movies['results']:
                print(movie['title'])
        elif ch == 3:
            movies = movie.getNow()
            for movie in movies['results']:
                print(movie['title'])
        elif ch == 4:
            movies = movie.getTopRated()
            for movie in movies['results']:
                print(movie['title'])
        else:
            print("Yanlis tuslama yaptiniz.")

