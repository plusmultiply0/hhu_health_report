from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from time import sleep
import time
import os

def health_report(chrdriver,usrid,pwd):
    try:
        driver = webdriver.Chrome(executable_path=chrdriver)
        driver.get("http://ids.hhu.edu.cn/amserver/UI/Login?goto=http://form.hhu.edu.cn/pdc/form/list")
        # user id
        driver.find_element(By.ID, "IDToken1").send_keys(usrid)
        # password and enter
        driver.find_element(By.ID, "IDToken2").send_keys(pwd+Keys.ENTER)
        # wait for page loaded
        sleep(2)
        #click the element
        ac2 = driver.find_element_by_css_selector("body > div:nth-child(1) > div:nth-child(4) > div > section > section > div > a > div.datav-ren-arrow")
        ActionChains(driver).move_to_element(ac2).click(ac2).perform()
        # wait for page loaded
        sleep(3)
        # finish the report 
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(1)
        driver.execute_script("var finish = document.querySelector('#saveBtn');finish.click();")
        sleep(3)
        # wait for page loaded
        nowdate = str(time.strftime('%Y.%m.%d %H.%M.%S',time.localtime(time.time())))+".png"
        # save successful shot
        driver.get_screenshot_as_file(nowdate)
        sleep(1)
        driver.quit()
    except Exception:
        print(str(Exception))
        print("Something unexpected happened")

# 从环境变量中读取
# Chromedriver 的系统路径
chrdriver = os.getenv('CHROME_DRIVER_PATH')
# 用户名
usrid = os.getenv('USER_ID')
# 密码
pwd = os.getenv('USER_PASSWORD')

if __name__=='__main__':
    health_report(chrdriver,usrid,pwd)
