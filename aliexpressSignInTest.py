from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import *
from aliexpressUserInfo import eMail, passWord
import time

class AliExpress:

  def __init__(self, eMail, passWord):
    self.browser = webdriver.Chrome()
    self.email = eMail
    self.password = passWord

  def goLoginPage(self):
    self.browser.get("https://best.aliexpress.com")
    time.sleep(5)

    signInVisible = self.browser.find_element_by_css_selector("#nav-user-account > div.user-account-info > div > span.account-unsigned > a:nth-child(1)")
    ActionChains(self.browser).click(signInVisible).perform()

  def goSignInBox(self):
    time.sleep(3)
    self.browser.find_element_by_css_selector('#fm-login-id').send_keys(self.email)
    self.browser.find_element_by_css_selector('#fm-login-password').send_keys(self.password)

    if (self.browser.find_element(By.CSS_SELECTOR, '#nc_1_n1z')):
      slider = self.browser.find_element(By.CSS_SELECTOR, '#nc_1_n1z') 
      move = ActionChains(self.browser)
      move.click_and_hold(slider).move_by_offset(75,0).perform()

    else:
      signIn = self.browser.find_element_by_css_selector("#login-form > div.fm-btn > button")
      ActionChains(self.browser).click(signIn).perform()

userDeniz = AliExpress(eMail, passWord)
userDeniz.goLoginPage()
userDeniz.goSignInBox()