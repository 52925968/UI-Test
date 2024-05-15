from time import sleep

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_chromedriver():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")
    driver.find_element(By.XPATH, '//*[@id="form"]/span[1]/span[1]').click()
    driver.find_element(By.XPATH,"//*[@id='form']/div/div[2]/div[2]/input").click()
        # send_keys("D:/pycharm/pythonProject/PC-UI/img/baidu.png")

    sleep(10)



