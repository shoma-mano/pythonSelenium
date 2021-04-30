import time
import chromedriver_binary
from selenium import webdriver
from testparts_module import kokyakuopen,Login
from test_module import HoujinTourokuTest,TorihikisakiTourokuTest,SeikyuSakiTourokuTest,TorimatomeKigyouHozonTest
from test_module import HoujinSakuzyoTest,HoujinHensyuTest
from common_module import TestDataObject,reportexcel
from testcode_module import postslacktest


# #chromeドライバー取得
# driver = webdriver.Chrome()
# driver.get('https://it.stellamock.com/#/tglogin')

# #ログイン画面を開いてログイン
# Login.login(driver)


# #結果報告
# reportexcel.excute(data)



#取纏企業新規保存テスト
#TorimatomeKigyouHozonTest.test(driver,data)

#取引先登録テスト
#TorihikisakiTourokuTest.test(driver,data)

#請求先登録テスト
##SeikyuSakiTourokuTest.test(driver,data)