import time
import chromedriver_binary
from selenium import webdriver
from common_module import move,sendkey,DetectError,Count,ex,postslack,Screenshot,Today,scroll,DetectSuccess


today=Today.today

#入力項目（エクセルから入力可能にする予定）

#企業ID
companyID="990"+today

#法人基本CD
houjin_kihon_CD = "HJ990"+today

#取引先名
torihikisakimei="取引先"+companyID

#カナ取引先名
kanatorihikisakimei="トリヒキサキ"

#連携会計取引先CD
renkeikaikeitorihikisakiCD="K"+companyID

#期待結果（期待結果が含まれていれば成功）
expectedmessage="登録"


def test(driver):
    #取引先登録テスト


    #取引先一覧メニューに移動
    move.excute(driver,"/html/body/app-root/app-main-layout/div/sa-navigation/aside/nav/ul/li[3]/ul/li[3]/a")
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0210/ps-container/div/ps-panel/div/div/div/div/div[2]/button[2]")

    #法人基本CD入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0220/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/div/form/div[1]/div[1]/div[2]/div/p-autocomplete/span/input",houjin_kihon_CD)
    # houjin_kihon_CD_element=driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0220/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/div/form/div[1]/div[1]/div[2]/div/p-autocomplete/span/input")
    # houjin_kihon_CD_element.send_keys(houjin_kihon_CD)
    time.sleep(3)

    #企業ID入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0220/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/div/form/div[2]/div[1]/div[2]/input",companyID)
    # kigyouID=driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0220/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/div/form/div[2]/div[1]/div[2]/input")
    # kigyouID.send_keys(companyID)

    #取引先名入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0220/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/div/form/div[3]/div[1]/div[2]/input",torihikisakimei)
    # torihikisakimei=driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0220/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/div/form/div[3]/div[1]/div[2]/input")
    # torihikisakimei.send_keys("取引先"+companyID)

    #取引先名(カナ）入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0220/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/div/form/div[3]/div[3]/div[2]/input",kanatorihikisakimei)
    # torihikisakimei=driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0220/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/div/form/div[3]/div[3]/div[2]/input")
    # torihikisakimei.send_keys("トリヒキサキ")

    #取引先区分
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0220/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/div/form/div[4]/div[1]/div[2]/p-dropdown/div/div[2]/span")

    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0220/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/div/form/div[4]/div[1]/div[2]/p-dropdown/div/div[4]/div/ul/p-dropdownitem[2]/li/span")
    #driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0220/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/div/form/div[4]/div[1]/div[2]/p-dropdown/div/div[4]/div/ul/p-dropdownitem[2]/li/span").click()
    
    #連携会計取引先CD入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0220/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/div/form/div[6]/div[1]/div[2]/input",renkeikaikeitorihikisakiCD)


    #imgフォルダにスクリーンショットを保存
    torihikisakitouroku=Count.makeCountObj("取引先登録",expectedmessage)
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
    DetectSuccess.excute(driver,torihikisakitouroku)


    #imgフォルダにスクリーンショットを保存
    Screenshot.excute(driver,torihikisakitouroku)
    time.sleep(3)


    #excelフォルダにhoujinエクセル作成
    ex.make_xl(torihikisakitouroku)


    #slack報告
    postslack.SendToSlack(torihikisakitouroku,"取引先登録")
