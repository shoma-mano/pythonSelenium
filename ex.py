import openpyxl
from openpyxl.drawing.image import Image


def make_xl(sheetname):
    # ワークブックを新規作成する
    book = openpyxl.Workbook()

    # シートを取得し名前を変更する
    sheet = book.active
    sheet.title = sheetname

    # 範囲を指定してセルを取得する
    cells = sheet['A1':'B3']
    i = 0
    for row in cells:
        for cell in row:
            cell.value = i # セルに値を設定する
            i += 1

    img = Image("img.png")
    img.width = 72 * 7
    img.height = 25 * 10
    sheet.add_image(img, 'D1')

    # ワークブックに名前をつけて保存する
    book.save("excel\\"+sheetname+'.xlsx')

make_xl("test")