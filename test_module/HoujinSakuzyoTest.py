from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from common_module import move,sendkey,DetectError,Count,ex,postslack,Screenshot,Today,scroll,DetectSuccess

#日付文字列取得（12/1ならtodayは1201となる)
today=Today.get()

#入力事項


#期待結果（期待結果が含まれていれば成功）
expectedmessage="処理成功しました"

def test(driver,data):

    #企業ID
    companyID=data.companyID

    #法人基本CD
    houjin_kihon_CD =data.houjin_kihon_CD

    #法人削除テスト
    #法人ページに移動
    move.excute(driver,"/html/body/app-root/app-main-layout/div/sa-navigation/aside/nav/ul/li[3]/ul/li[2]")
    
    #法人CD入力して検索
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0110/ps-container/div/ps-body/div/div/input",houjin_kihon_CD)
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0110/ps-container/div/ps-body/div/div/button")

    # 編集ページに移動
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0110/ps-container/div/ps-body/div/ps-panel[2]/div/div[2]/div/p-table/div/div/div/div[2]/table/tbody/tr/td[1]/button/i")

    #imgフォルダにスクリーンショットを保存
    houjinsakuzyo=Count.makeCountObj("法人削除",expectedmessage)
    time.sleep(1)
    Screenshot.excute(driver,houjinsakuzyo)
    
    #無効化
    scroll.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-footer/div/div[1]/button[2]")
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-footer/div/div[1]/button[2]")
    move.excute(driver,"/html/body/app-dialog/div/div/div[3]/button[1]")

    #結果チェック
    DetectSuccess.excute(driver,houjinsakuzyo)
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0110/ps-container/div/ps-body/div/div/input",houjin_kihon_CD)
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0110/ps-container/div/ps-body/div/div/button")

    #imgフォルダにスクリーンショットを保存
    Screenshot.excute(driver,houjinsakuzyo)
    
    #excelフォルダにhoujinエクセル作成
    ex.make_xl(houjinsakuzyo)

    #slack報告
    postslack.SendToSlack(houjinsakuzyo,"法人削除")
