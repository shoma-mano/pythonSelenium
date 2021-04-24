from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from common_module import move,sendkey,DetectError,Count,ex,postslack,Screenshot,Today,scroll,DetectSuccess

today=Today.today

#期待結果（期待結果が含まれていれば成功）
expectedmessage="登録しました"

#取纏幹事企業登録テスト
def test(driver,data):

    #企業ID
    companyID=data.companyID

    #法人基本CD
    houjin_kihon_CD = data.houjin_kihon_CD

    #請求先CD
    seikyusakiCD=data.seikyusakiCD

    #連携会計取引先CD
    renkeikaikeitorihikisakiCD=data.renkeikaikeitorihikisakiCD

    #会計取引先CD
    kaikeitorihikisakiCD=data.kaikeitorihikisakiCD

    #請求先名
    seikyusakiMei=data.seikyusakiMei

    #請求先営業担当者
    seikyusakieigyotantousya=data.seikyusakieigyotantousya

    #請求先営業責任者
    seikyusakieigyosekininsya=data.seikyusakieigyosekininsya

    #請求先一覧ページに移動
    move.excute(driver,"/html/body/app-root/app-main-layout/div/sa-navigation/aside/nav/ul/li[3]/ul/li[4]/a/span")
    
    #新規ページに移動
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0310/ps-container/div/ps-body/div/ps-panel/div/div/div/ps-footer/div/div/button[2]")

    # 請求先CD入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0320/ps-container/div/ps-body/div/form/ps-panel[1]/div/div[2]/div/div[1]/div[1]/div[2]/input",seikyusakiCD)
    
    #請求先名入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0320/ps-container/div/ps-body/div/form/ps-panel[1]/div/div[2]/div/div[2]/div[1]/div[2]/input",seikyusakiMei)
    
    #会計取引先CD入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0320/ps-container/div/ps-body/div/form/ps-panel[1]/div/div[2]/div/div[3]/div[1]/div[2]/input",kaikeitorihikisakiCD)

    #imgフォルダにスクリーンショットを保存
    seikyusakitouroku=Count.makeCountObj("請求先","登録",expectedmessage)
    Screenshot.excute(driver,seikyusakitouroku)
    time.sleep(1)

    #入金予定日入力
    scroll.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0320/ps-container/div/ps-body/div/form/ps-panel[3]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/p-dropdown/div/div[2]/span")
    time.sleep(1)
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0320/ps-container/div/ps-body/div/form/ps-panel[3]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/p-dropdown/div/div[2]/span")
    #当月選択
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0320/ps-container/div/ps-body/div/form/ps-panel[3]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/p-dropdown/div/div[4]/div/ul/p-dropdownitem[1]/li")
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0320/ps-container/div/ps-body/div/form/ps-panel[3]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/p-dropdown/div/div[2]/span")
    #5日選択
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0320/ps-container/div/ps-body/div/form/ps-panel[3]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/p-dropdown/div/div[4]/div/ul/p-dropdownitem[1]/li")

    #締グループ入力
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0320/ps-container/div/ps-body/div/form/ps-panel[3]/div/div[2]/div/div[1]/div[3]/div[2]/p-dropdown/div/div[2]/span")
    #拠点選択
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0320/ps-container/div/ps-body/div/form/ps-panel[3]/div/div[2]/div/div[1]/div[3]/div[2]/p-dropdown/div/div[4]/div/ul/p-dropdownitem[1]/li/span")
 
    #請求書締日入力
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0320/ps-container/div/ps-body/div/form/ps-panel[3]/div/div[2]/div/div[2]/div[3]/div[2]/div/p-dropdown/div/div[2]/span")
    #20日選択
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0320/ps-container/div/ps-body/div/form/ps-panel[3]/div/div[2]/div/div[2]/div[3]/div[2]/div/p-dropdown/div/div[4]/div/ul/p-dropdownitem[1]/li")

    # 請求先営業担当者入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0320/ps-container/div/ps-body/div/form/ps-panel[3]/div/div[2]/div/div[3]/div[3]/div[2]/p-autocomplete/span/input",seikyusakieigyotantousya)
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0320/ps-container/div/ps-body/div/form/ps-panel[3]/div/div[2]/div/div[3]/div[3]/div[2]/p-autocomplete/span/div/ul/li")

    # 請求先営業責任者入力
    sendkey.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0320/ps-container/div/ps-body/div/form/ps-panel[3]/div/div[2]/div/div[4]/div[3]/div[2]/p-autocomplete/span/input",seikyusakieigyosekininsya)
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0320/ps-container/div/ps-body/div/form/ps-panel[3]/div/div[2]/div/div[4]/div[3]/div[2]/p-autocomplete/span/div/ul/li")

    #imgフォルダにスクリーンショットを保存
    Screenshot.excute(driver,seikyusakitouroku)
    time.sleep(1)
    
    # 登録
    scroll.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0320/ps-container/div/ps-footer/div/div[2]/button")
    move.excute(driver,"/html/body/app-root/app-main-layout/div/div/app-b15f0320/ps-container/div/ps-footer/div/div[2]/button")
    move.excute(driver,"/html/body/app-dialog/div/div/div[3]/button[1]")

    #エラー検出
    DetectSuccess.excute(driver,seikyusakitouroku,)

    #結果登録
    data.result[seikyusakitouroku.testname][seikyusakitouroku.testtype]=seikyusakitouroku.result

    #imgフォルダにスクリーンショットを保存
    Screenshot.excute(driver,seikyusakitouroku)
    time.sleep(1)

    #excelフォルダにhoujinエクセル作成
    ex.make_xl(seikyusakitouroku)

    #slack報告
    postslack.SendToSlack(seikyusakitouroku,"請求先登録")