import time
import selenium

def excute(driver,id):
    while True:
        try:
            cart=driver.find_element_by_id(id)
            cart.click()
            break
        except selenium.common.exceptions.NoSuchElementException:
            print("ok")
            time.sleep(0.1)