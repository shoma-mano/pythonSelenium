import time
import selenium

def excute(driver,xpath,message):
    while True:
        try:
            element=driver.find_element_by_xpath(xpath)
            element.send_keys(message)
            break
        except :
            print("loading...")
            time.sleep(0.1)