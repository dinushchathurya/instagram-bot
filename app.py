from selenium import webdriver
from selenium.webdriver.common import keys
import time

class InstagramBot():
  def __init__ (self,username, password):
     self.username = username
     self.password = password
     self.driver = webdriver.Chrome()

  def closebrowser(self):
    self.driver.close()

  def login(self):
    driver = self.driver
    driver.get("https://www.instagram.com/")
    time.sleep(2)
    login_button =driver.find_element_by_xpath("//a[a@href'accounts/login']")
    login_button.click()
    time.sleep(2)
    

andreyIG = InstagramBot("username","password")
andreyIG.login()
     

