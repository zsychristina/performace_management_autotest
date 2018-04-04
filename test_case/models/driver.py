#coding=utf-8
from selenium import webdriver
#from selenium.webdriver import Remote

#启动浏览器驱动
def browser():
    driver = webdriver.Chrome()
    return driver

if __name__ == '__main__':
    dr = browser()
    dr.get("http://10.138.14.131:9000/ui#/")
