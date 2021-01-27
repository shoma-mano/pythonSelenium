import time
import selenium

def excute(driver,name,message):
    while True:
        try:
            cart=driver.find_element_by_name(name)
            cart.send_keys(message)
            break
        except selenium.common.exceptions.NoSuchElementException:
            print("ok")
            time.sleep(0.2)