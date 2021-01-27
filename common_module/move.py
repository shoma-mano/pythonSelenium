import time
import selenium

def excute(driver,xpath):
    while True:
        try:
            element=driver.find_element_by_xpath(xpath)
            element.click()
            break
        except :
            print("loading...")
            time.sleep(0.1)