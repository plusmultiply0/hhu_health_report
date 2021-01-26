from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from time import sleep
import time
import os


# 从环境变量中读取
def import_env():
    if os.path.exists('.env'):
        print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            key, value = var[0].strip(), var[1].strip()
            os.environ[key] = value
    usrid = os.environ.get('USER_ID')
    pwd = os.environ.get('USER_PASSWORD')
    return [usrid,pwd]


def health_report():
        try:
                # 无需设置chrome driver路径
                driver = webdriver.Chrome()
                driver.get("http://ids.hhu.edu.cn/amserver/UI/Login?goto=http://form.hhu.edu.cn/pdc/form/list")
                # 获取.env中保存的用户名和密码
                [usrid,pwd] = import_env()
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
                # 将截图保存在 png文件夹 下
                driver.get_screenshot_as_file('png\\'+nowdate)
                sleep(1)
                print("今日打卡成功，请查看成功打卡截图！")
                driver.quit()
        except Exception:
                print(str(Exception))
                print("Something unexpected happened")

if __name__=='__main__':
    health_report()
