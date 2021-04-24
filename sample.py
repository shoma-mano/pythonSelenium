import time
import chromedriver_binary
from selenium import webdriver

# グーグルでポピュラーソフトと検索するプログラム、URL→https://www.google.com/
driver = webdriver.Chrome()
#開きたいページのURLを入力
driver.get('https://www.google.com/')
time.sleep(4)
#グーグルの検索欄要素を取得 /html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input
search_box = driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input")
#入力欄にテキストを入力
search_box.send_keys('ポピュラーソフト')
#検索
search_box.submit()
#検索結果が表示されるまで待機します
time.sleep(5)
#ポピュラーソフトの検索結果の要素を取得 /html/body/div[7]/div[2]/div[9]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/a
ps_hp=driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[9]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/a")
#検索結果をクリック
ps_hp.click()