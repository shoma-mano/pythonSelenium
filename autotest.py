import time
import datetime
import chromedriver_binary
from selenium import webdriver
import openpyxl
import ex #make_xl(機能名)で/excelにexcelファイルを作成
import postslack #SendToSlack(エクセル名、メッセージ名）slackに報告
import TorihikisakiTourokuTest
import HoujinTourokuTest
import scroll
import Login
import Today

#日付文字列取得（12/1ならtodayは1201となる)
today=Today.get()

#企業ID
companyID="109"+today

#chromeドライバー取得
driver = webdriver.Chrome()
driver.get('https://it.stellamock.com/#/tglogin')

#ログイン画面を開いてログイン
time.sleep(2)
Login.login(driver)


#顧客情報メニューを開く
kokyaku = driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/sa-navigation/aside/nav/ul/li[3]/a/span")
kokyaku.click()
time.sleep(2)

#法人登録テスト
HoujinTourokuTest.test(driver)

#取引先登録テスト
#TorihikisakiTourokuTest.test(driver)

