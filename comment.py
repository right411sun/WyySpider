from selenium import webdriver
from config import *
from time import sleep

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.switch_to.frame('g_iframe')
with open('test.txt','w',encoding='utf-8') as file:
    for page in range(1, 28):
        print("第{}页评论获取中".format(page))
        file.write("\n" + "第{}页评论获取中".format(page) + "\n")
        comment = driver.find_elements_by_xpath('//*[@class="itm"]/div[2]/div[1]/div')
        for i in comment:
            file.write(i.text + "\n")
        element = driver.find_element_by_link_text('下一页')
        driver.execute_script("arguments[0].click();", element)
        sleep(0.5)
driver.switch_to.default_content()
driver.quit()
