import time
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get('https://www.google.com/')
time.sleep(5)
element = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div/div/div[1]/div[1]/a")
element.click()
ac = ActionChains(driver)
ac.move_to_element(element).move_by_offset(0, 0).click().perform()
time.sleep(5)


