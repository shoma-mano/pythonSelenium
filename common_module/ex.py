import openpyxl
from openpyxl.drawing.image import Image
import datetime
from common_module import Today

today=Today.get()



def make_xl(kinoumei):
    # ワークブックを新規作成する
    book = openpyxl.Workbook()

    # シートを取得し名前を変更する
    sheet = book.active
    sheet.title = kinoumei.name

    # 範囲を指定してセルを取得する
    # cells = sheet['A1':'B3']
    # i = 0
    # for row in cells:
    #     for cell in row:
    #         cell.value = i # セルに値を設定する
    #         i += 1
    kinoumei.number+=1
    for i in range(1,kinoumei.number):
        img = Image("img\\"+kinoumei.name+str(i)+".png")
        img.width = 72 * 7
        img.height = 38 * 10
        sheet.add_image(img, 'D'+str(25*(i-1)+1))

    # ワークブックに名前をつけて保存する
    book.save("excel\\"+kinoumei.name+kinoumei.testtype+'.xlsx')
    print("エクセルを作成しました")