import requests  

class GitHub:
    def __init__(self):
        self.api_URL = "https://api.github.com"
        self.token = "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" #! 7 Days (start: 09.12.21)

    def getUser(self, username):
        response = requests.get(self.api_URL+"/users/"+username)
        return response.json()

    def getRepositories(self, username):
        response = requests.get(self.api_URL+"/users/"+username+"/repos")
        return response.json()

    def createRepository(self, repoName, descripton, homepage, bool):
        response = requests.post(self.api_URL+"/user/repos?access_token="+self.token, json={
            "name": repoName,
            "description": descripton,
            "homepage": homepage,
            "private": bool,
            "has_issues": True,
            "has_projects": True,
            "has_wiki" : True
        })
        return response.json()


github = GitHub()


while True:
    print("\n"+"*"*50)
    ch = int(input("1- Find User\n2- Get Repositories\n3- Create Repositories\n4- Exits\n\nChoose: "))

    if ch == 4:
        break
    else:
        if ch == 1:
            username = input("\n>> Username: ")
            result = github.getUser(username=username)
            print(f"\nname: {result['name']}\nPublic Repos: {result['public_repos']}\nFollower: {result['followers']}")
        elif ch == 2:
            username = input("\n>> Username: ")
            result = github.getRepositories(username=username)
            for repo in result:
                print(repo['name'])
        elif ch == 3:
            repoName = input("Repo Name: ")
            
            descripton = input("Description: ")
            
            homepage = input("Have you homepage? (Yes/No): ")
            if (homepage == "Y") or (homepage == "y"): homepage = input("Homepage: ")
            else: homepage = ""
            
            bool = input("For Private! (True/False): ") 
            if (bool == "T") or (bool == "t"): bool = True
            else: bool = False
            
            github.createRepository(repoName=repoName, descripton=descripton, homepage=homepage, bool=bool)
        else:
            print("Your choose is False.")