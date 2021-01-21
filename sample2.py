import time
import datetime
import chromedriver_binary
from selenium import webdriver
import openpyxl
import ex.py

#日付文字列取得（12/1ならtodayは1201となる)
s=datetime.datetime.now()

month=str(s.month)
day=str(s.day)

if len(str(s.month))==1:
    month=str(0)+str(s.month)

if len(str(s.day))==1:
    day=str(0)+str(s.day)

today=month+day


# ワークブックを新規作成する
book = openpyxl.Workbook()


# シートを取得し名前を変更する
sheet = book.active
sheet.title = 'First sheet'



driver = webdriver.Chrome()
driver.get('https://it.stellamock.com/#/tglogin')

# pw入力
userpw= driver.find_element_by_name("password")
userpw.send_keys("pf01@@@@")

# id入力
userid= driver.find_element_by_name("userId")
userid.send_keys("unyo@TG")


# ログイン
login = driver.find_element_by_id("loginButton")
login.click()
print("CAPCHA認証の文字をクリックしましたか？(y/n)")
str = input()
login.click()
time.sleep(5)

# 顧客情報クリック
kokyaku = driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/sa-navigation/aside/nav/ul/li[3]/a/span")
kokyaku.click()
time.sleep(2)

# 法人一覧クリック
houjin = driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/sa-navigation/aside/nav/ul/li[3]/ul/li[2]")
houjin.click()
time.sleep(2)

# 新規作成クリック
shinki = driver.find_element_by_xpath("/html/body[@class='desktop-detected ng-tns-0-1 smart-style-9']/app-root/app-main-layout[@class='ng-star-inserted']/div[@class='ng-star-inserted']/div[@id='main']/app-b15f0110[@class='ng-star-inserted']/ps-container/div[@class='padding-20']/ps-body/div/ps-panel[@class='ng-tns-c91-4 ng-star-inserted']/div[@class='ng-tns-c91-4 panel']/div[@class='ng-tns-c91-4 panel-container']/div[@class='ng-tns-c91-4 ng-trigger ng-trigger-slideInOut ng-star-inserted panel-content']/div[@class='margin-b-10 ng-tns-c91-4']/div[2]/button[@class='btn btn-action'][2]")
shinki.click()
time.sleep(4)

# 法人基本CD
houjin_kihon_CD=driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/form/div/div[2]/div[1]/div[2]/input")
# houjinCD="HJ109"+today
# houjin_kihon_CD.send_keys(houjinCD)
houjin_kihon_CD.send_keys("HJ1090000")

# 法人名
houjin_mei=driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/form/div/div[3]/div[1]/div[2]/input")
houjin_mei.send_keys("test")

# 登録
houjin_touroku=driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-footer/div/div[2]/button")
houjin_touroku.click()
time.sleep(3)

sfile = driver.get_screenshot_as_file("C:\\Users\\mano-syou\\Desktop\\python\\img\\"+"img"+today+".png")
print(sfile)

# シートを取得し名前を変更する
sheet = book.active
sheet.title = today

