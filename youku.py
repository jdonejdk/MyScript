# -*- coding: UTF-8 -*-
import re
import os
import sys
import time
from lxml import etree
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

path = r""
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options,executable_path=path)
driver.get("https://list.youku.com/albumlist/show/id_18840618.html")

time.sleep(2)
# 最大化窗口
driver.maximize_window()
# 模拟鼠标滚动
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(2)
driver.execute_script('window.scrollTo(0,0)')
time.sleep(2)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(2)
driver.execute_script('window.scrollTo(0,0)')
time.sleep(2)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(2)
# 提取链接
r = driver.page_source
html = etree.HTML(r)
result = html.xpath('//div[@class="p-thumb"]/a/@href')
text = []
for i in result:
    text += re.findall(r"\//(.+?)\?",i)

print(text)
f = open("output.txt","w+")
for i in text:
    f.write("https://"+i+"\n")

f.close()
driver.close()
driver.quit()

# /html/body/div[2]/div/div[2]/div[2]/div[2]/div[38]/div/a
# /html/body/div[2]/div/div[2]/div[2]/div[2]/div[39]/div/a
# /html/body/div[2]/div/div[2]/div[2]/div[2]/div[69]/div/a