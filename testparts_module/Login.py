from selenium import webdriver
from common_module import sendkey_name,moveid
import time

def login(driver):
    # pw入力
    sendkey_name.excute(driver,"password","pf@@@@")
    # userpw= driver.find_element_by_name("password")
    # userpw.send_keys("pf01@@@@")

    # id入力
    sendkey_name.excute(driver,"userId","un@TG")
    # userid= driver.find_element_by_name("userId")
    # userid.send_keys("unyo@TG")

    #ログイン
    # login = driver.find_element_by_id("loginButton")
    # login.click()
    moveid.excute(driver,"loginButton")
    print("CAPCHA認証の文字をクリックしましたか？(y/n)")
    str = input()
    moveid.excute(driver,"loginButton")
