from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from common_module import move,sendkey,DetectError,Count,ex,postslack,Screenshot,Today,scroll,DetectSuccess,reportexcel
from common_module import DeleteText

#日付文字列取得
today=Today.get()

#期待結果（期待結果が含まれていれば成功）
expectedmessage="変更が完了しました"

def test(driver,data):
    #入力事項

    #企業ID
    companyID = data.companyID

    #法人基本CD
    houjin_kihon_CD = data.houjin_kihon_CD

    #法人名
    houjinMei = data.houjinMei+"編集済"

    #住所
    address = data.address

    #ビル名
    billMei = data.billMei

    #カナ法人名
    kanahoujinMei =data.kanahoujinMei

    #代表電話番号
    telNo = data.telNo


    #法人編集テスト
    #法人ページに移動
    move.excute(driver,"/html/body/app-root/app-main-layout/div/sa-navigation/aside/nav/ul/li[3]/ul/li[2]")
    
    # 法人基本CDで検索
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0110/ps-container/div/ps-body/div/div/input",houjin_kihon_CD)
    
    #検索クリック
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0110/ps-container/div/ps-body/div/div/button")
    
    #データ選択
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0110/ps-container/div/ps-body/div/ps-panel[2]/div/div[2]/div/p-table/div/div/div/div[2]/table/tbody/tr[1]/td[1]/button/i")

    #編集
    time.sleep(2)
    #imgフォルダにスクリーンショットを保存
    houjinhensyu=Count.makeCountObj("法人","更新",expectedmessage)
    Screenshot.excute(driver,houjinhensyu)

    # 法人名入力
    DeleteText.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/form/div/div[3]/div[1]/div[2]/input")
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/form/div/div[3]/div[1]/div[2]/input",houjinMei)

    # (郵便番号のみ自動入力不可能)
    # yuubin=driver.find_element_by_xpath("/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/form/div/div[4]/div[1]/div[2]/div/input")
    # yuubin.click()
 
    # 住所入力
    #sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/form/div/div[5]/div[1]/div[2]/input",address)

    #ビル名入力
    #sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/form/div/div[6]/div[1]/div[2]/input",billMei)

    # カナ法人名入力
    #sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/form/div/div[3]/div[3]/div[2]/input",kanahoujinMei)

    # 代表電話番号入力
    #sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-body/div/ps-panel/div/div[2]/div/form/div/div[4]/div[3]/div[2]/input",telNo)
    
    #imgフォルダにスクリーンショットを保存
    Screenshot.excute(driver,houjinhensyu)
    

    # 変更
    scroll.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-footer/div/div[2]/button")
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0120/ps-container/div/ps-footer/div/div[2]/button")
    move.excute(driver,"/html/body/app-dialog/div/div/div[3]/button[1]")

    #結果チェック
    DetectSuccess.excute(driver,houjinhensyu)

    #結果登録
    data.result[houjinhensyu.testname][houjinhensyu.testtype]=houjinhensyu.result
    
    #imgフォルダにスクリーンショットを保存
    Screenshot.excute(driver,houjinhensyu)

    #excelフォルダにhoujinエクセル作成
    ex.make_xl(houjinhensyu)


    #slack報告
    postslack.SendToSlack(houjinhensyu,"法人更新")
