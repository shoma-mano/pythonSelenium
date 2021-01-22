import chromedriver_binary
from selenium import webdriver
import time
import datetime

driver = webdriver.Chrome()
driver.get('https://www.amazon.co.jp/dp/B08QRC14GH/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B08QRC14GH&pd_rd_w=dGJKf&pf_rd_p=89a7aa0c-0b87-4868-af20-8288efcf20fc&pd_rd_wg=oNVRn&pf_rd_r=NP971A1VCZEJ811H9G0C&pd_rd_r=b6f0870d-164b-4dde-a21e-dad3f5438d37&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExTkpQUjMzTEE3NVZaJmVuY3J5cHRlZElkPUEwMzc5OTE1MTBJS0ZETVZURVRPTSZlbmNyeXB0ZWRBZElkPUFIWk9ZQVBJRVVWQkwmd2lkZ2V0TmFtZT1zcF9kZXRhaWwmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl')

time.sleep(4)

button=driver.find_element_by_xpath("/html/body/div[2]/header/div/div[1]/div[3]/div/a[2]")
button.click()

time.sleep(3)

tel=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]")
tel.send_keys("08040742284")

next=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[2]/span/span/input")
next.click()

time.sleep(3)

pw=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[1]/input")
pw.send_keys("46466man")

login=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[2]/span/span/input")
login.click()

price=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div[5]/div[4]/div[6]/div[1]/div/table/tbody/tr/td[2]/span[1]")
nowprice=(int)price.text.replace(chr(65509),"").replace(",","")
print(price.text.replace(chr(65509),"").replace(",",""))