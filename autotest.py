import time
import chromedriver_binary
from selenium import webdriver
from testparts_module import kokyakuopen,Login
from test_module import HoujinTourokuTest,TorihikisakiTourokuTest,SeikyuSakiTourokuTest,TorimatomeKigyouHozonTest


#chromeドライバー取得
driver = webdriver.Chrome()
driver.get('https://it.stellamock.com/#/tglogin')

#ログイン画面を開いてログイン
Login.login(driver)

#顧客情報メニューを開く
kokyakuopen.excute(driver)

#法人登録テスト
HoujinTourokuTest.test(driver)

#取引先登録テスト
TorihikisakiTourokuTest.test(driver)

#請求先登録テスト
SeikyuSakiTourokuTest.test(driver)

#取纏企業新規保存テスト
TorimatomeKigyouHozonTest.test(driver)
