from selenium import webdriver
from selenium.webdriver.common import keys
import os
# import wmi


opts = webdriver.ChromeOptions()
opts.add_experimental_option("excludeSwitches", ["enable-logging"])
opts.add_argument('--user-data-dir=C:\zoomdont_dumyfile')
# opts.add_argument('headless')

driver = webdriver.Chrome
# process_name = wmi.WMI().win32_process.name

def linkget(link):
    engin = driver("./chromedriver.exe", options=opts)
    engin.get(link)
    engin.implicitly_wait(10)
    # driver.quit()


    # if 'Zoom' in 줌 켜져있는지 확인할꺼임? 
if __name__ == '__main__':
    pass