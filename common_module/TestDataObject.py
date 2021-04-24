from common_module import Today
import random
today=Today.get()

#乱数生成
number3=(str)(random.randint(500,999))
number4=(str)(random.randint(5000,9999))
number5=(str)(random.randint(40000,99999))

class makeTestDataObj:
    #企業ID(7桁)
    companyID="AT"+number5
    #法人基本CD(9桁)
    houjin_kihon_CD = "HJAT"+number5
    #法人名
    houjinMei = houjin_kihon_CD+"test"
    #住所
    address = "自動テスト住所"+today
    #ビル名
    billMei = "ジドウテストビル"+today
    #カナ法人名
    kanahoujinMei ="ジドウテスト"+today
    #代表電話番号
    telNo = "000000000000"
    #取引先名
    torihikisakiMei = "自動テスト取引先"+companyID
    #カナ取引先名
    kanatorihikisakiMei="ジドウテストトリヒキサキ"
    #連携会計取引先CD
    renkeikaikeitorihikisakiCD="K"+companyID
    #請求先CD
    seikyusakiCD=number3+today
    #会計取引先CD
    kaikeitorihikisakiCD=renkeikaikeitorihikisakiCD
    #請求先名
    seikyusakiMei="自動テスト請求先"+companyID
    #請求先営業担当者
    seikyusakieigyotantousya="営業者02211"
    #請求先営業責任者
    seikyusakieigyosekininsya="営業者02211"      
    #メールアドレス
    email="ms2@com"
    #取纏契約名
    torimatomekeiyakuMei="自動テスト取纏"+companyID
    #郵便番号
    yuubinCD="1330056"
    #テスト実施数
    number=0
    #テスト結果
    result={"法人":{"登録":"","読込":"","更新":"","削除":""},
            "取引先":{"登録":"","読込":"","更新":"","削除":""},
            "請求先":{"登録":"","読込":"","更新":"","削除":""},
    }