import time
import chromedriver_binary
from selenium import webdriver
from testparts_module import kokyakuopen,Login
from test_module import HoujinTourokuTest,TorihikisakiTourokuTest,SeikyuSakiTourokuTest,TorimatomeKigyouHozonTest
from test_module import HoujinSakuzyoTest,HoujinHensyuTest
from common_module import TestDataObject,reportexcel

#chromeドライバー取得
driver = webdriver.Chrome()
driver.get('https://it.stellamock.com/#/tglogin')

#ログイン画面を開いてログイン
Login.login(driver)

#顧客情報メニューを開く
kokyakuopen.excute(driver)

#テストデータ作成
data=TestDataObject.makeTestDataObj()

#法人登録テスト
HoujinTourokuTest.test(driver,data)

#法人編集テスト
HoujinHensyuTest.test(driver,data)

#法人削除(無効化)テスト
HoujinSakuzyoTest.test(driver,data)

#結果報告
reportexcel.excute(data)



#取纏企業新規保存テスト
#TorimatomeKigyouHozonTest.test(driver,data)

#取引先登録テスト
#TorihikisakiTourokuTest.test(driver,data)

#請求先登録テスト
##SeikyuSakiTourokuTest.test(driver,data)