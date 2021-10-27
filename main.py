#
#import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import os
#import wget
from selenium.webdriver.common.keys import Keys
import time
#設定瀏覽器位置(看自身chrome的版本做下載)
PATH = "C:/Users/c8902/Desktop/chromedriver_win32/chromedriver_win32/chromedriver.exe"
browser = webdriver.Chrome(PATH)
#設定瀏覽器前往網址
#Url = 'https://chrome.google.com/webstore/detail/downthemall/nljkibfhlpcnanjgbnlnbjecgicbjkge'
#browser.get(Url)
#time.sleep(5)
#button = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div[2]/div')
#button.click()
time.sleep(1)
#button.send_keys(Keys.ARROW_LEFT)
#time.sleep(1)
#button.send_keys(Keys.RETURN)
url = 'https://www.instagram.com/'
browser.get(url)
#等待並定位輸入帳號密碼的區塊
username = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, 'username'))
)
password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, 'password'))
)
#先將區塊淨空兵書入帳密
username.clear()
password.clear()
username.send_keys("帳號")
password.send_keys("密碼")



#定位並點擊登入按鈕
login = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
login.click()

with open("欲查詢範本 ",mode="r",encoding="utf-8") as file:
    for line in file:
        #定位並輸入關鍵字之後回車鍵查詢
        search = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
        )
        keyword = line.replace('\n', ' ')
        #keyword = 'huangjie_official'
        search.send_keys(keyword)
        time.sleep(2)
        search.send_keys(Keys.RETURN)
        time.sleep(2)
        search.send_keys(Keys.RETURN)

        time.sleep(3)
        f = open('阿滴'+keyword+'.txt','w')
        #定位追蹤中人數區塊
        found = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a'))
        )
        # 定位追蹤中人數並顯示
        num = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').get_attribute("innerHTML")
        #print("顯示人數:"+num)
        #因追蹤中人數區塊可有五到六個名稱故除之以便下拉
        #a = int(num)//5
        a = int(num.replace(',', ''))//5
        #點擊追蹤中人數區塊
        #if found = 0:
        found.click()
        #等待並定位追蹤中人數區塊的出現
        WebDriverWait(browser, 10).until(lambda d: d.find_element_by_css_selector('div[role="dialog"]'))

        #等待三秒後下拉追蹤中人數區塊---讓追蹤者區塊完整出現
        for i in range(1,a+2):
            time.sleep(3)
            browser.execute_script('''
                var fDialog = document.querySelector('div[role="dialog"] .isgrP');
                fDialog.scrollTop = fDialog.scrollHeight
                ''')

            #定位追蹤中人數區塊的追蹤者名稱
        titles = browser.find_elements_by_class_name("FPmhX")

            #測試是否正確顯示追蹤中人數的變數
        b = 0

            # 顯示追蹤者的個別名稱
        for title in titles:
            b = b + 1
            print("https://www.instagram.com/" + title.text + "/", file=f)
            #print(title.text, file=f)
            if b >= int(num):
                break


            #print("https://www.instagram.com/"+title.text+"/")
        print("顯示人數:" + num, file=f)
        print("確實帳號:",b,file=f)
        c = int(num.replace(',', ''))
        d = c-b
        print('隱私帳號:',d,file=f)
        numb = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').get_attribute("title")
        print("被追蹤人數:"+numb,file=f)
        f.close()
        browser.back()


        #print("確實帳號:",b)

        #c = int(num)
        #d = c-b
        #print('隱私帳號:',d)

        #numb = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').get_attribute("title")
        #print("被追蹤人數:"+numb)


        #path = os.path.join(keyword)
        #os.mkdir(path)
        #count = 0
        #for title in titles :
        #    save_as = os.path.join(path, keyword +".txt")
        #    wget.download(title.text, save_as)
        #    count += 1

        #num = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').get_attribute("innerHTML")

















        #time.sleep(3)
        #browser.quit()
        #var scroll = setInterval(function(){window.scrollTo(0, document.body.scrollHeight)},2000);

        #滑到下方

        #for i in range(5):
        #    browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        #    time.sleep(5)

        #path = os.path.join(keyword)
        #os.mkdir(path)