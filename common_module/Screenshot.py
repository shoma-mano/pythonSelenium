from common_module import Today

def excute(driver,kinoumei):
    kinoumei.number+=1
    print(kinoumei.name+str(kinoumei.number)+"枚目のスクリーンショット")
    sfile = driver.get_screenshot_as_file("C:\\Users\\mano-syou\\Desktop\\python\\img\\"+kinoumei.name+str(kinoumei.number)+".png")

