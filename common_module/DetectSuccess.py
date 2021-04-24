import time

def excute(driver,testmei):
  for i in range(10):
    try:
      message= driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/p")
      print(message.text)
      if (testmei.expectedmessage in message.text):
        print("期待通りの結果が出力されました")
        testmei.result="〇"
        testmei.message=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/p").text
        break
      else:
        testmei.message=message.text
        time.sleep(0.7)
      
    except:
      time.sleep(0.7)