from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep,time
from bs4 import BeautifulSoup

def do(xpath:str,name:str,action:str,keys:str=None):
    elements = []
    while elements == []:
        elements = browser.find_elements(By.XPATH,xpath)
    print("%s定位成功!"%name)
    element = elements[0]
    match action:
        case "click":
            element.click()
            print("%s点击成功!" % name)
        case "type":
            element.send_keys(keys)
            print("%s输入成功!" % name)

if __name__ == "__main__":
    browser = webdriver.Firefox()
    browser.get("https://uis.cqut.edu.cn/unified_identity_logon/#/login")
    do(xpath="//*[@id='app']/div/div[1]/div[2]/div/div[2]/form/div[1]/div/div/input",name="账号",action="type",keys="account")
    do(xpath="//*[@id='app']/div/div[1]/div[2]/div/div[2]/form/div[2]/div/div/input",name="密码",action="type",keys="password")
    do(xpath="//*[@id='app']/div/div[1]/div[2]/div/div[2]/button",name="登录",action="click")
    do(xpath="/html/body/div/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div/section/div[3]/div[2]/div/div/div/div/div",name="本科生选课",action="click")
    handles = browser.window_handles
    browser.switch_to.window(handles[-1])
    do(xpath="/html/body/div[1]/div/div/div[2]/div/div[1]/div/div/div/div/span/button[1]",name="查询",action="click")
    sleep(1)
    do(xpath="/html/body/div[1]/div/div/div[2]/div/div[1]/div/div/div/div/span/button[1]",name="查询",action="click")
    content = browser.page_source
    