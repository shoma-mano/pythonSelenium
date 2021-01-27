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

companyID="996"+today

#取纏幹事企業登録テスト
def test(driver):

    #movinostar契約一覧ページに移動
    move.excute(driver,"/html/body/app-root/app-main-layout/div/sa-navigation/aside/nav/ul/li[3]/ul/li[5]/a")
    
    #新規ページに移動
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b60f0410/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/div/div[2]/p-tieredmenu/div/p-tieredmenusub/ul/li/a")
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b60f0410/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/div/div[2]/p-tieredmenu/div/p-tieredmenusub/ul/li/p-tieredmenusub/ul/li[3]/a")

    # 取引先（企業ID)入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b60f0610_1/ps-container/div/ps-body/div/div/ps-panel[2]/div/div[2]/div/div/div[1]/div/div/p-calendar/span/input",companyID)

    # 契約開始年月入力
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b60f0610_1/ps-container/div/ps-body/div/div/ps-panel[2]/div/div[2]/div/div/div[1]/div/div/p-calendar/span/input")
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b60f0610_1/ps-container/div/ps-body/div/div/ps-panel[2]/div/div[2]/div/div/div[1]/div/div/p-calendar/span/div/div[2]/a[1]")
 
    # 契約名入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b60f0610_1/ps-container/div/ps-body/div/div/ps-panel[2]/div/div[2]/div/div/div[2]/div[1]/div/input","取り纏め"+companyID)

    # 住所入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b60f0610_1/ps-container/div/ps-body/div/div/ps-panel[2]/div/div[2]/div/div/div[4]/div[1]/div/input","住所"+companyID)

    
    # 代表電話番号入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b60f0610_1/ps-container/div/ps-body/div/div/ps-panel[2]/div/div[2]/div/div/div[4]/div[1]/div/input","0000000000")


    # 氏名入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b60f0610_1/ps-container/div/ps-body/div/div/ps-panel[3]/div/div[2]/div/div/div[2]/div[1]/div/input","U"+companyID)

    # ユーザID入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b60f0610_1/ps-container/div/ps-body/div/div/ps-panel[2]/div/div[2]/div/div/div[4]/div[1]/div/input","U"+companyID)
　　
    # メールアドレス入力
    print("メールアドレスを入力しましたか？(y/n)")
    str = input()


    #imgフォルダにスクリーンショットを保存
    houjintouroku=Count.makeCountObj("法人登録")
    Screenshot.excute(driver,houjintouroku)
    time.sleep(1)
    

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
    ex.make_xl(houjintouroku,houjintouroku.number)


    #slack報告
    postslack.SendToSlack(houjintouroku,"法人登録")