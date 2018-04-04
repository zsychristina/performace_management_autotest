#coding=utf-8

from selenium import webdriver
from .driver import browser
import os,unittest

#定义MyTest()类用于继承unittest.TestCase类
class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
