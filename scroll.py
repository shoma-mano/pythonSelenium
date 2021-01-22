from selenium.webdriver.common.action_chains import ActionChains
import chromedriver_binary
from selenium import webdriver

def scroll(driver,target):
    actions = ActionChains(driver)
    actions.move_to_element(target)
    actions.perform()
