import time

def excute(driver,kinoumei,expected):
  for i in range(5):
    try:
      message= driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/p")
      print(message)
      if (expected in message.text):
        print("期待通りの結果が出力されました")
        kinoumei.result="成功"
        kinoumei.message=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/p").text
        break
      if ('エラー' in message.text):
        print("エラーを検出しました")
        kinoumei.result="エラー"
        kinoumei.message=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/p").text
        break
    except:
      time.sleep(0.7)
