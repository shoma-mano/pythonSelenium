import time
import chromedriver_binary
from selenium import webdriver
from common_module import move,sendkey,DetectError,Count,ex,postslack,Screenshot,Today,scroll,DetectSuccess

today=Today.today

#企業ID
companyID="988"+today

#メールアドレス
email="ms2@com"

#契約名
keiyakuMei="取り纏め"+companyID

#郵便番号
yuubinCD="1330056"

#期待結果（期待結果が含まれていれば成功）
expectedmessage="登録しました"

#取纏幹事企業登録テスト
def test(driver):

    #movinostar契約一覧ページに移動
    move.excute(driver,"/html/body/app-root/app-main-layout/div/sa-navigation/aside/nav/ul/li[3]/ul/li[5]/a")
    
    #新規ページに移動
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b60f0410/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/div/div[2]/p-tieredmenu/div/p-tieredmenusub/ul/li/a")
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b60f0410/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/div/div[2]/p-tieredmenu/div/p-tieredmenusub/ul/li/p-tieredmenusub/ul/li[3]/a")

    # 取引先（企業ID)入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b60f0610_1/ps-container/div/ps-body/div/div/ps-panel[1]/div/div[2]/div/div/div[2]/p-autocomplete/span/input",companyID)
    time.sleep(3)

    # 契約開始年月入力
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b60f0610_1/ps-container/div/ps-body/div/div/ps-panel[2]/div/div[2]/div/div/div[1]/div/div/p-calendar/span/input")
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b60f0610_1/ps-container/div/ps-body/div/div/ps-panel[2]/div/div[2]/div/div/div[1]/div/div/p-calendar/span/div/div[2]/a[1]")
 
    # 契約名入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b60f0610_1/ps-container/div/ps-body/div/div/ps-panel[2]/div/div[2]/div/div/div[2]/div[1]/div/input",keiyakuMei)

    # 住所入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b60f0610_1/ps-container/div/ps-body/div/div/ps-panel[2]/div/div[2]/div/div/div[4]/div[1]/div/input","住所"+companyID)
    
    #郵便番号入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b60f0610_1/ps-container/div/ps-body/div/div/ps-panel[2]/div/div[2]/div/div/div[3]/div[1]/div/input",yuubinCD)

    # 代表電話番号入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b60f0610_1/ps-container/div/ps-body/div/div/ps-panel[2]/div/div[2]/div/div/div[4]/div[3]/div/input","0000000000")
    time.sleep(1)

    # 氏名入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b60f0610_1/ps-container/div/ps-body/div/div/ps-panel[3]/div/div[2]/div/div/div[2]/div[1]/div/input","U"+companyID)

    # ユーザID入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b60f0610_1/ps-container/div/ps-body/div/div/ps-panel[3]/div/div[2]/div/div/div[1]/div[1]/div/input","U"+companyID)

    # メールアドレス入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b60f0610_1/ps-container/div/ps-body/div/div/ps-panel[3]/div/div[2]/div/div/div[3]/div[3]/div/input",email)



    #imgフォルダにスクリーンショットを保存
    torimatometouroku=Count.makeCountObj("取纏企業保存",expectedmessage)
    Screenshot.excute(driver,torimatometouroku)
    time.sleep(1)
    

    # 保存
    scroll.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b60f0610_1/ps-container/div/ps-body/div/ps-footer/div/div[2]/button")
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b60f0610_1/ps-container/div/ps-body/div/ps-footer/div/div[2]/button")
    move.excute(driver,"/html/body/app-dialog/div/div/div[3]/button[1]")
 

    #エラー検出
    DetectSuccess.excute(driver,torimatometouroku)

    #imgフォルダにスクリーンショットを保存
    Screenshot.excute(driver,torimatometouroku)
    time.sleep(3)


    #excelフォルダにhoujinエクセル作成
    ex.make_xl(torimatometouroku)


    #slack報告
    postslack.SendToSlack(torimatometouroku,"取纏企業保存")