import time
import chromedriver_binary
from selenium import webdriver
import openpyxl
import ex #make_xl(シート名,機能名)　で　/excelにexcelファイルを作成
import postslack
import scroll
import Count
import Screenshot
import Today
from selenium.webdriver.common.action_chains import ActionChains
import DetectError


today=Today.today


#入力事項
companyID="999"+today
houjin_kihon_CD = "HJ999"+today


def test(driver):
    #取引先登録テスト


    #取引先一覧メニューに移動
    torihikisaki = driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/sa-navigation/aside/nav/ul/li[3]/ul/li[3]/a")
    torihikisaki.click()
    time.sleep(3)
    sakusei = driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0210/ps-container/div/ps-panel/div/div/div/div/div[2]/button[2]")
    sakusei.click()
    time.sleep(3)

    #法人基本CD入力
    houjin_kihon_CD_element=driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0220/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/div/form/div[1]/div[1]/div[2]/div/p-autocomplete/span/input")
    houjin_kihon_CD_element.send_keys(houjin_kihon_CD)
    time.sleep(4)

    #企業ID入力
    kigyouID=driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0220/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/div/form/div[2]/div[1]/div[2]/input")
    kigyouID.send_keys(companyID)

    #取引先名入力
    torihikisakimei=driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0220/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/div/form/div[3]/div[1]/div[2]/input")
    torihikisakimei.send_keys("取引先"+companyID)

    #取引先名(カナ）入力
    torihikisakimei=driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0220/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/div/form/div[3]/div[3]/div[2]/input")
    torihikisakimei.send_keys("トリヒキサキ")

    #取引先区分
    driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0220/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/div/form/div[4]/div[1]/div[2]/p-dropdown/div/div[2]/span").click()
    time.sleep(4)
    driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0220/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/div/form/div[4]/div[1]/div[2]/p-dropdown/div/div[4]/div/ul/p-dropdownitem[2]/li/span").click()
    
    #imgフォルダにスクリーンショットを保存
    torihikisakitouroku=Count.makeCountObj("取引先登録")
    Screenshot.excute(driver,torihikisakitouroku)
    time.sleep(3)


    #登録
    touroku=driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0220/ps-container/div/ps-footer/div/div[2]/button")
    scroll.scroll(driver,touroku)
    touroku.click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/app-dialog/div/div/div[3]/button[1]").click()

    time.sleep(3)

    #エラー検出
    DetectError.excute(driver,torihikisakitouroku)


    #imgフォルダにスクリーンショットを保存
    Screenshot.excute(driver,torihikisakitouroku)
    time.sleep(3)


    #excelフォルダにhoujinエクセル作成
    ex.make_xl(torihikisakitouroku.name,torihikisakitouroku.number)


    #slack報告
    postslack.SendToSlack(torihikisakitouroku,"取引先登録")
