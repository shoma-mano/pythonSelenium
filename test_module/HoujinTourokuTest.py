from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from common_module import move,sendkey,DetectError,Count,ex,postslack,Screenshot,Today,scroll,DetectSuccess

#日付文字列取得（12/1ならtodayは1201となる)
today=Today.get()

#入力事項

#企業ID
companyID="990"+today

#法人基本CD
houjin_kihon_CD = "HJ990"+today

#期待結果（期待結果が含まれていれば成功）
expectedmessage="登録しました"

def test(driver):
    #法人登録テスト
    #法人ページに移動
    move.excute(driver,"/html/body/app-root/app-main-layout/div/sa-navigation/aside/nav/ul/li[3]/ul/li[2]")
    
    #新規ページに移動
    move.excute(driver,"/html/body[@class='desktop-detected ng-tns-0-1 smart-style-9']/app-root/app-main-layout[@class='ng-star-inserted']/div[@class='ng-star-inserted']/div[@id='main']/app-b15f0110[@class='ng-star-inserted']/ps-container/div[@class='padding-20']/ps-body/div/ps-panel[@class='ng-tns-c91-4 ng-star-inserted']/div[@class='ng-tns-c91-4 panel']/div[@class='ng-tns-c91-4 panel-container']/div[@class='ng-tns-c91-4 ng-trigger ng-trigger-slideInOut ng-star-inserted panel-content']/div[@class='margin-b-10 ng-tns-c91-4']/div[2]/button[@class='btn btn-action'][2]")

    # 法人基本CD入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/form/div/div[2]/div[1]/div[2]/input",houjin_kihon_CD)

    # 法人名入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/form/div/div[3]/div[1]/div[2]/input",houjin_kihon_CD+"test")

    # 本社所在地入力(郵便番号のみ自動入力不可能)
    # yuubin=driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/form/div/div[4]/div[1]/div[2]/div/input")
    # yuubin.click()
 
    # 本社所在地入力 住所
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/form/div/div[5]/div[1]/div[2]/input","住所"+today)

    # 本社所在地入力 ビル名
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/form/div/div[6]/div[1]/div[2]/input","ビル"+today)

    # 本社所在地入力 カナ法人名
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/form/div/div[3]/div[3]/div[2]/input","テスト"+today)

    # 本社所在地入力　代表電話番号
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/form/div/div[4]/div[3]/div[2]/input","00000000000")
    
    #imgフォルダにスクリーンショットを保存
    houjintouroku=Count.makeCountObj("法人登録",expectedmessage)
    Screenshot.excute(driver,houjintouroku)
    

    # 登録
    houjin_touroku=driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-footer/div/div[2]/button")
    scroll.scroll(driver,houjin_touroku)
    houjin_touroku.click()
    time.sleep(1)
    move.excute(driver,"/html/body/app-dialog/div/div/div[3]/button[1]")

    #結果チェック
    DetectSuccess.excute(driver,houjintouroku)

    #imgフォルダにスクリーンショットを保存
    Screenshot.excute(driver,houjintouroku)

    #excelフォルダにhoujinエクセル作成
    ex.make_xl(houjintouroku)


    #slack報告
    postslack.SendToSlack(houjintouroku,"法人登録")
