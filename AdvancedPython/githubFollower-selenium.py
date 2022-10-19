
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Github:
    def __init__(self):
        self.followers = []
        self.browser = webdriver.Chrome()

    def signIn(self, username, password):
        self.username = username
        self.password = password
        self.browser.get("http://github.com/login")
        time.sleep(2)
        self.browser.find_element_by_name('login').send_keys(self.username)
        self.browser.find_element_by_name('password').send_keys(self.password)
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='login']/div[4]/form/div/input[12]").click()
        time.sleep(1)
        self.browser.maximize_window()

    def getFollower(self):
        self.browser.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/summary").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/details-menu/a[1]").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='js-pjax-container']/div[2]/div/div[1]/div/div[2]/div[3]/div[2]/div[3]/div/a[1]").click()
        time.sleep(2)
        
        index = 1
        for i in range(int(self.browser.find_element_by_xpath("//*[@id='js-pjax-container']/div[2]/div/div[1]/div/div[2]/div[3]/div[2]/div[3]/div/a[1]/span").text)) :
            self.followers.append(self.browser.find_element_by_xpath(f"//*[@id='js-pjax-container']/div[2]/div/div[2]/div[2]/div/div[{index}]/div[2]/a/span[2]").text)
            index += 1

github = Github()


while True:
    ch = int(input("1- Giris\n2- Cikis\n\nSecim: "))
    if ch == 2:
        break
    else:
        if ch == 1:
            username = input("Username: ")
            password = input("Password: ")
            github.signIn(username=username, password=password)
            github.getFollower()
            print(github.followers)
            break
        else:
            print("Yanlis islem")


