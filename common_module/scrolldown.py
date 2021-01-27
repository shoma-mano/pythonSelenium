from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def excute(driver):
    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()