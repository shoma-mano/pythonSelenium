
def excute(kinoumei,driver):
    kinoumei.number+=1
    print(kinoumei.number)
    sfile = driver.get_screenshot_as_file("C:\\Users\\mano-syou\\Desktop\\python\\img\\"+today+kinoumei+str(kinoumei.number)+".png")

