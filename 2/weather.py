from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import shutil
import os

def getLastestFilename():
    path='C:\\Users\\User\\Downloads'
    try:
        filename=max([f for f in os.listdir(path)],\
            key=lambda x:os.path.getmtime(os.path.join(path,x)))
    except:
        filename=max([f for f in os.listdir(path)],\
            key=lambda x:os.path.getmtime(os.path.join(path,x))) 
    return filename

def change(finalName):
    while True:
        filename=getLastestFilename()
        if filename.endswith('.csv'):
            break
    path='C:\\Users\\User\\Downloads'
    shutil.move(f'{path}\\{filename}',f'{path}\\{finalName}')

#找到網站
browser=webdriver.Chrome('./2/chromedriver.exe')
browser.get('https://e-service.cwb.gov.tw/HistoryDataQuery/')

#按下北方鈕
while True:
    try:
        browser.find_element_by_id('Button_North').click()
        break
    except:
        pass
time.sleep(2)

#找尋縣市
for item in Select(browser.find_element_by_id('stationCounty')).options:
    #print(item.text)
    if item.text.find('新北市')!=-1:
        Select(browser.find_element_by_id('stationCounty'))\
            .select_by_visible_text(item.text)
            

#找尋觀測站
for item in Select(browser.find_element_by_id('station')).options:
    Select(browser.find_element_by_id('station'))\
        .select_by_visible_text(item.text)

    print(item.text)
#改變日期&按下查詢鈕
    browser.find_element_by_id('datepicker').send_keys('2021-01-01')
    browser.find_element_by_id('doquery').click()

#下載天氣檔案
    windows=browser.window_handles
    browser.switch_to_window(windows[-1])
    browser.find_element_by_xpath\
        ("//input[@src='images/downloadCSV_2.png']").click()
    browser.close()
    browser.switch_to_window(windows[0])
    
    time.sleep(2)
#改名
    change(f"{item.text}.csv")

    