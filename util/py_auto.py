# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2018/6/30 0:57'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyautogui, time
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
url=''+input('请输入编号：')
driver.get('')
driver.maximize_window()
time.sleep(30)
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'bigImg')))
page_ele = driver.find_element_by_xpath('//*[@id="time"]/span[1]')
page_count_raw = page_ele.text
page_count =int(page_count_raw.split(' ')[1])

screenWidth, screenHeight = pyautogui.size()
# 获取当前鼠标位置
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
next_ele = driver.find_element_by_id('next')
for i in range(page_count):

    pyautogui.rightClick()
    pyautogui.press('v')
    time.sleep(10)
    pyautogui.press('enter')
    next_ele.click()
    time.sleep(10)
    pyautogui.moveTo(screenWidth / 2, screenHeight / 2)


