import openpyxl
from openpyxl.drawing.image import Image
import datetime

#日付文字列取得（12/1ならtodayは1201となる)
s=datetime.datetime.now()

month=str(s.month)
day=str(s.day)

if len(str(s.month))==1:
    month=str(0)+str(s.month)

if len(str(s.day))==1:
    day=str(0)+str(s.day)

today=month+day



def make_xl(kinoumei,number):
    # ワークブックを新規作成する
    book = openpyxl.Workbook()

    # シートを取得し名前を変更する
    sheet = book.active
    sheet.title = kinoumei

    # 範囲を指定してセルを取得する
    # cells = sheet['A1':'B3']
    # i = 0
    # for row in cells:
    #     for cell in row:
    #         cell.value = i # セルに値を設定する
    #         i += 1
    for i in range(1,number)
        img = Image("img\\"+today+kinoumei+i+".png")
        img.width = 72 * 7
        img.height = 38 * 10
        sheet.add_image(img, 'D'+str(25*(i-1)))

    # ワークブックに名前をつけて保存する
    book.save("excel\\"+today+kinoumei+'.xlsx')