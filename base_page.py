import os
import time
import traceback
from datetime import datetime
from time import sleep

import yaml
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MobileBy(object):
    pass


class BasePage:
    _driver = None
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        # if driver is None:
        #     chrome_options = Options()
        #     self._driver = webdriver.Chrome(options=chrome_options)
        #
        # else:
        #     self._driver = driver
        # #
        # # if self._base_url != "":
        # #     self.driver.get(self._base_url)
        #
        # self._driver.get("http://192.168.1.78:12139/#/login")
        # self._driver.implicitly_wait(5)

        self._driver = driver


    def openurl(self, url):
        self._driver.get(url)
        time.sleep(5)

    def wait_for_click(self,locator):
        WebDriverWait(self._driver, 1).until(expected_conditions.element_to_be_clickable(locator))

    def login(self, username, password):
        #从yaml中读取固定的登录用户名 密码 登录按键地址
        with open("./resource_yaml/login.yaml", encoding="utf_8") as f:
            loc = yaml.safe_load(f)
        el = loc["MetaBase"]["username"].split(',')
        username_loc = tuple(el)
        self.input(username_loc, username)

        el = loc["MetaBase"]["password"].split(',')
        password_loc = tuple(el)
        self.input(password_loc, password)

        el = loc["MetaBase"]["login"].split(',')
        login_loc = tuple(el)
        self.click(login_loc)

        return True


    def find(self,locator):
        # logging.info(f'find: {locator}')
        # print(locator)
        try:
            elem = self._driver.find_element(*locator)
            # elem = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(locator))
        except NoSuchElementException:
            print("元素不存在")
            return None
        else:
            # print("元素存在")
            return elem



    def finds(self,locator):
        # logging.info(f'find: {locator}')
        try:
            self._driver.find_elements(*locator)
        except NoSuchElementException:
            print("元素不存在")
            return None
        else:
            elems = self._driver.find_elements(*locator)
            print("找到的元素是：", elems)
            # res_list = []
            # for ele in elems:
            #     res_list.append(ele.text)
            # return res_list
            return elems


    def click(self,locator):
        # logging.info(f'find_and_click: {locator}')
        elem = self.find(locator)
        if elem==None:
            print("元素不存在")
            return False
        else:
            # print("元素存在")
            elem.click()
            sleep(2)
            return True


    def click_word(self,word):
        text = str('//*[@text="' + word + '"]')
        print(text)
        elem=self.find((By.XPATH, text))
        if elem==None:
            print("元素不存在")
            return False
        else:
            print("元素存在")
            elem.click()
            sleep(2)
            return True

    def clear(self, locator):
        # logging.info(f'find: {locator}')
        try: elem = self._driver.find_element(*locator)
        except NoSuchElementException:
            # print("元素不存在")
            return None
        else:
            # print("元素存在")
            elem.clear()
            return True


    def clear_delete(self, locator):
        try:
            elem = self._driver.find_element(*locator)
        except NoSuchElementException:
            return None
        else:
            elem.send_keys(Keys.CONTROL, "a")
            elem.send_keys(Keys.DELETE)
            return True

    def input(self, locator, text):
        # logging.info(f'find: {locator}')
        elem = self.find(locator)
        if elem==None:
            print("元素不存在")
            return False
        else:
            # print("元素存在")
            elem.send_keys(text)
            return True

    def scroll(self,text):
        try: elem=self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector()'
                                                                     f'.text("{text}").instance(0));')
        except NoSuchElementException:
            # print("元素不存在")
            return False
        else:
            # print("元素存在")
            return  True
        #
        # return self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector()'
        #                                                              f'.text("{text}").instance(0));')

    def back(self,num=1):
        back_list = ['left_btn', 'mLeftImg','iv_finish','cancel_search']
        for i in range(num):
            for back in back_list:
                back_str = str('//*[@resource-id="com.pinsmedical.pinslife:id/' + back + '"]')
                # print(back_str)
                back_elem=self.find((By.XPATH, back_str))
                if back_elem is not None:
                    print(i,back,back_elem)
                    back_elem.click()
                    break
                elif back==back_list[-1]:
                    print('返回错误')
                    return  False
        return True



    # def click_pic(self,locator):
    #     # logging.info(f'find: {locator}')
    #     return  self.driver.find_element(*locator)



    def get_text(self,locator):
        # logging.info(f'find_and_click: {locator}')
        elem=self.find(locator)
        if elem==None:
            # print("元素不存在")
            return False
        else:
            # print("元素存在")
            word=elem.text
            sleep(2)
            # print(word)
            return word


    def get_attribute(self,locator):
        # logging.info(f'find_and_click: {locator}')
        elem = self.find(locator)
        if elem == None:
            # print("元素不存在")
            return False
        else:
            # print("元素存在")
            word = elem.get_attribute('value')
            sleep(2)
            print("元素value存在", word)
            if word == None:
                word = elem.get_attribute("src")
                print("元素src存在", word)
            return word

    def get_texts(self, locator):
        # logging.info(f'find_and_click: {locator}')
        num = 0
        while num <3:
            elem = self.finds(locator)
            if elem:
                break
            else:
                num +=1

        if elem==None:
            # print("元素不存在")
            return False
        else:
            # print("元素存在")
            # print(len(elem))
            words = [x.text for x in elem]
            words = ','.join(words)
            sleep(2)
            return words


    def show(self, locator):
        try: elem=self._driver.find_element(*locator)
        except NoSuchElementException:
            # print("元素不存在")
            return False
        else:
            # print("元素存在")
            return True

    def show_word(self,word):
        text= str('//*[@text="' + word + '"]')
        # print(text)
        elem=self.find((By.XPATH, text))
        if elem==None:
            # print("元素不存在")
            return False
        else:
            # print("元素存在")
            # time.sleep(2)
            return True


    def count(self, locator):
        lens=['']
        try: elem=self._driver.find_elements(*locator)
        except NoSuchElementException:
            # print("元素不存在")
            return None
        else:
            elems = self._driver.find_elements(*locator)
            # print("元素存在")
            print(elems)
            lens = len(elems)
            return lens

    def toast(self, text, timeout=3, poll_frequency=0.5):
        try:
            # toast_loc = ('xpath', './/*[contains(@text,"%s")]' % text)
            toast_loc = (By.XPATH, ".//*[contains(@text,%s)]"% text)
            WebDriverWait(self._driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
            print('toast:', text)
            return True
        except TimeoutException:
            print('toast有误')
            return False


    #定位下拉框，并点击目标选项
    """
    locator:路径
    text：希望选中的元素
    """
    def select_box(self, locator, text):
        options = self.finds(locator)
        # print("options:", options)
        for option in options:
            print(option.text, text, type(option.text), type(text))
            if option.text == text:
                option.click()
                break


