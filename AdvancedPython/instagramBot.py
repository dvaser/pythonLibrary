
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import os

def menu():
    while True:
        ch = int(input("1- Giris\n2- Cikis\n\nSecim: "))
        if ch == 2:
            break
        else:
            if ch == 1:
                username = input("Username: ")
                password = input("Password: ")
                insta.login(username=username, password=password)
                insta.getFollowers()
                
                break
            else:
                print("Yanlis islem")

class Instagram:
    def __init__(self):
        self.insta_URL = "https://www.instagram.com/"
        self.login_URL = "https://www.instagram.com/accounts/login/"
        self.twoFactor_URL = "https://www.instagram.com/accounts/login/two_factor?next=%2F"

    def twoFactor(self):
        phoneCode = int(input("Telefona gelen kod: "))
        self.browser.find_element_by_name("verificationCode").send_keys(phoneCode)
        self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/section/main/div/div/div[1]/div/form/div[2]/button").click()

    def getUnfollowers(self):
        self.getFollowers()
        time.sleep(10)
        self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div[2]/button").click()
        time.sleep(5)
        self.getFollowing()
        time.sleep(10)
        self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div[2]/button").click()
        time.sleep(20)
        for fr in self.followers:
            for i, fg in enumerate(self.following):
                if fr == fg:
                    fg[i] = ""

        self.unfollowers = []
        for user in self.following:
            if user != "":
                self.unfollowers.append(user)

        print(self.unfollowers)

    def getFollowers(self):
        self.followers = [] 
        followersCount = int(self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span").text)
        
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(5)

        dialog = self.browser.find_element_by_css_selector("div[role='dialog'] ul")
        count = len(dialog.find_elements_by_css_selector("li"))
        
        action = webdriver.ActionChains(self.browser)
        
        while True:
            dialog.click()
            action.key_down(Keys.PAGE_DOWN).key_up(Keys.PAGE_DOWN).perform()
            time.sleep(2)

            newCount = len(dialog.find_elements_by_css_selector("li"))   

            if count != followersCount:
                count = newCount
                time.sleep(1)
            else:
                break

        for li in dialog.find_elements_by_css_selector("li"):
            self.followers.append(li.find_element("a").text)


        print(self.followers)

    def getFollowing(self):
        self.following = [] 
        followingCount = int(self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span").text)
        
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a").click()
        time.sleep(5)

        dialog = self.browser.find_element_by_css_selector("div[role='dialog'] ul")
        count = len(dialog.find_elements_by_css_selector("li"))

        action = webdriver.ActionChains(self.browser)
        
        while True:
            dialog.click()
            action.key_down(Keys.PAGE_DOWN).key_up(Keys.PAGE_DOWN).perform()
            time.sleep(2)

            newCount = len(dialog.find_elements_by_css_selector("li"))   

            if count != followingCount:
                count = newCount
                time.sleep(1)
            else:
                break

        for li in dialog.find_elements_by_css_selector("li"):
            self.following.append(li.find_element("a").text)

    def login(self, username, password):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.username = username
        self.password = password

        self.browser.get(self.login_URL)
        time.sleep(2)
        self.browser.find_element_by_name("username").send_keys(self.username)
        self.browser.find_element_by_name("password").send_keys(self.password) # .send_keys(Keys.ENTER)
        time.sleep(1)

        if (len(self.username) >= 1) and (len(self.password) >= 6):
            self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click()

        time.sleep(5)
        if self.browser.current_url == self.login_URL:
            os.system("cls")
            menu()

        while self.browser.current_url == self.twoFactor_URL:
            self.twoFactor()

        self.browser.get(self.insta_URL+self.username)
        # self.browser.get(self.insta_URL)
        # time.sleep(2)
        # self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
        # time.sleep(1)
        # self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/section/nav/div[2]/div/div/div[3]/div/div[6]/span").click()
        # time.sleep(1)
        # self.browser.find_element_by_xpath("//*[@id='f16a2f3564f1db8']/div/div/div").click()

insta = Instagram()
menu()

