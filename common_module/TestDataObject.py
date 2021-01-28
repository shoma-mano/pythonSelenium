from common_module import Today
import random
today=Today.get()
number=(str)(random.randint(500,999))

class makeTestDataObj:
    #企業ID
    companyID=number+today
    #法人基本CD
    houjin_kihon_CD = "HJ"+number+today
    #法人名
    houjinMei = houjin_kihon_CD+"test"
    #住所
    address = "住所"+today
    #ビル名
    billMei = "ビル"+today
    #カナ法人名
    kanahoujinMei ="テスト"+today
    #代表電話番号
    telNo = "000000000000"
    #取引先名
    torihikisakiMei = "取引先"+companyID
    #カナ取引先名
    kanatorihikisakiMei="テストトリヒキサキ"
    #連携会計取引先CD
    renkeikaikeitorihikisakiCD="K"+companyID
    #請求先CD
    seikyusakiCD=number+today
    #会計取引先CD
    kaikeitorihikisakiCD=renkeikaikeitorihikisakiCD
    #請求先名
    seikyusakiMei="請求先"+companyID
    #請求先営業担当者
    seikyusakieigyotantousya="営業者02211"
    #請求先営業責任者
    seikyusakieigyosekininsya="営業者02211"      
    #メールアドレス
    email="ms2@com"
    #取纏契約名
    torimatomekeiyakuMei="取り纏め"+companyID
    #郵便番号
    yuubinCD="1330056"
    #テスト結果
    result={"法人":{"登録":"","読込":"","更新":"","削除":""}}
    #pullreq