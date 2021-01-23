from selenium import webdriver
import time

def login(driver):
    # pw入力
    userpw= driver.find_element_by_name("password")
    userpw.send_keys("pf01@@@@")

    # id入力
    userid= driver.find_element_by_name("userId")
    userid.send_keys("unyo@TG")

    #ログイン
    login = driver.find_element_by_id("loginButton")
    login.click()
    print("CAPCHA認証の文字をクリックしましたか？(y/n)")
    str = input()
    login.click()
    time.sleep(5)
