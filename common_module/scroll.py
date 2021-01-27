from selenium.webdriver.common.action_chains import ActionChains
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def scroll(driver,target):
    actions = ActionChains(driver)
    actions.move_to_element(target)
    actions.perform()

    driver.execute_script("window.scrollTo(0, 1000)")

def excute(driver,target):
    element=driver.find_element_by_xpath(target)
    actions = ActionChains(driver)
    actions.move_to_element(element)
    actions.perform()
    driver.execute_script("window.scrollTo(0, 1080)")
    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
