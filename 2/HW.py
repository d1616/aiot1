from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


username ='ttu410602215'
loginUrl='http://aiot.kaitechstudio.com'
counter=''

browser=webdriver.Chrome('./2/chromedriver.exe')
browser.get(loginUrl)

browser.find_element_by_name('userID').send_keys(username)
browser.find_element_by_name('userID').send_keys(Keys.ENTER)

time.sleep(2)

while True:
    counter=browser.find_element_by_id('succesCounter').text

    Q1=browser.find_element_by_id('Q1').get_attribute('value')
    Q2=browser.find_element_by_id('Q2').get_attribute('value')

    Q1_answer=Q1.replace(' ','').replace('|',username)
    
    print(Q1)
    #Q1_answer=Q1
    
    print(Q2)
    Q2s=Q2.split(' ')
    print(Q2s)
    if Q2s[1] == '+':
        ans=int(Q2s[0])+int(Q2s[2])
    elif Q2s[1] == '-':
        ans=int(Q2s[0])-int(Q2s[2])
    elif Q2s[1] == '*':
        ans=int(Q2s[0])*int(Q2s[2])
    elif Q2s[1] == '%':
        ans=int(Q2s[0])%int(Q2s[2])
    
    print(Q2)
    Q2_answer=ans
    
    browser.find_element_by_id('Q1a').send_keys(Q1_answer)
    browser.find_element_by_id('Q2a').send_keys(Q2_answer)
    browser.find_element_by_id('btnSubmit').click()
    
    time.sleep(1)
    
    counter=browser.find_element_by_id('succesCounter').text
    if counter=='200':
        browser.refresh()
        break