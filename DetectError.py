def excute(driver,kinoumei):
  message= driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/span")
  if ('エラー' in message.text):
        print("エラーを検出しました")
        kinoumei.result="エラー"
        kinoumei.message=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/p").text