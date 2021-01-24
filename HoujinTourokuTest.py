from selenium import webdriver
import ex #make_xl(シート名,機能名)　で　/excelにexcelファイルを作成
import postslack
import scroll
import Today
from selenium.webdriver.common.action_chains import ActionChains
import time
import Screenshot
import Count
import DetectError

#日付文字列取得（12/1ならtodayは1201となる)
today=Today.get()

#入力事項
companyID="999"+today
houjin_kihon_CD = "HJ999"+today

def test(driver):
    #法人登録テスト

    #法人登録ページに移動
    houjin = driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/sa-navigation/aside/nav/ul/li[3]/ul/li[2]")
    houjin.click()
    time.sleep(2)

    shinki = driver.find_element_by_xpath("/html/body[@class='desktop-detected ng-tns-0-1 smart-style-9']/app-root/app-main-layout[@class='ng-star-inserted']/div[@class='ng-star-inserted']/div[@id='main']/app-b15f0110[@class='ng-star-inserted']/ps-container/div[@class='padding-20']/ps-body/div/ps-panel[@class='ng-tns-c91-4 ng-star-inserted']/div[@class='ng-tns-c91-4 panel']/div[@class='ng-tns-c91-4 panel-container']/div[@class='ng-tns-c91-4 ng-trigger ng-trigger-slideInOut ng-star-inserted panel-content']/div[@class='margin-b-10 ng-tns-c91-4']/div[2]/button[@class='btn btn-action'][2]")
    shinki.click()
    time.sleep(4)



    # 法人基本CD入力
    houjin_kihon_CD_element=driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/form/div/div[2]/div[1]/div[2]/input")
    # houjinCD="HJ109"+today
    # houjin_kihon_CD.send_keys(houjinCD)
    houjin_kihon_CD_element.send_keys(houjin_kihon_CD)


    # 法人名入力
    houjin_mei=driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/form/div/div[3]/div[1]/div[2]/input")
    houjin_mei.send_keys("test")


    # 本社所在地入力
    yuubin=driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/form/div/div[4]/div[1]/div[2]/div/input")
    yuubin.click()
    time.sleep(2)

    driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/form/div/div[4]/div[1]/div[2]/div/button").click()
 
    # 本社所在地入力 住所
    address=driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/form/div/div[5]/div[1]/div[2]/input")
    address.send_keys("住所"+today)


    # 本社所在地入力 ビル名
    bill=driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/form/div/div[6]/div[1]/div[2]/input")
    bill.send_keys("ビル"+today)


    # 本社所在地入力 カナ法人名
    houjinmei_kana=driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/form/div/div[3]/div[3]/div[2]/input")
    address.send_keys("テスト")


    # 本社所在地入力　代表電話番号
    tel=driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/form/div/div[4]/div[3]/div[2]/input")
    tel.send_keys("00000000000")
    

    #imgフォルダにスクリーンショットを保存
    houjintouroku=Count.makeCountObj("法人登録")
    Screenshot.excute(driver,houjintouroku)
    time.sleep(3)
    

    # 登録
    houjin_touroku=driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-footer/div/div[2]/button")
    scroll.scroll(driver,houjin_touroku)
    houjin_touroku.click()
    time.sleep(1)
    houjin_touroku=driver.find_element_by_xpath("/html/body/app-dialog/div/div/div[3]/button[1]")
    houjin_touroku.click()
    time.sleep(3)

    #エラー検出
    DetectError.excute(driver,houjintouroku)

    #imgフォルダにスクリーンショットを保存
    Screenshot.excute(driver,houjintouroku)
    time.sleep(3)


    #excelフォルダにhoujinエクセル作成
    ex.make_xl(houjintouroku.name,houjintouroku.number)


    #slack報告
    postslack.SendToSlack(houjintouroku,"法人登録")
