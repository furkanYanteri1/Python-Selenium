# Furkan Yanteri Hürriyet emlak QA test Case

import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#===========================================
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#================================================
from selenium.webdriver.chrome import options
#==================================================
from selenium.webdriver.support.select import Select



#---------------->SETUP<------------------#

mobile_emulation = {
    "deviceName":"iPhone 8"
    }

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(
    executable_path="C:\Program Files (x86)\chromedriver.exe", options=chrome_options
)
url = "https://www.hurriyetemlak.com"
driver.get(url)
driver.maximize_window()#tam ekran olsun
try:
    kapat_kampanya = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "modal__close"))
    )
finally:
    kapat_kampanya.click()




#---------------->TEST<------------------#

driver.get(driver.current_url+"kiralik")

#filtrele Dropdown
try:
    dropdown = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[3]/div/button[2]"))
    )
finally:
    dropdown.click()
# driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[3]/div/button[2]")
#cerez kapat
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/section[1]/div[2]/select").click()
#ankara sec
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/section[1]/div[2]/select/option[3]").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/section[1]/div[2]/select").click()
#cankaya sec
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/section[1]/section[1]/div[1]").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/section[1]/section[1]/div[2]/div[2]/div[2]/li[7]").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/section[1]/section[1]/div[2]/div[2]/button/div").click()
#scroll down
driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)/4);")
#2+1
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/section[4]/section/div").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/section[4]/section/div[2]/div[2]/ul/li[3]").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/section[4]/section/div[2]/div[2]/button").click()
#scroll down
driver.execute_script("window.scrollTo(0, (document.body.scrollHeight));")
#site icerisinde
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/section[15]/label/input").click()
#sonuclari goster
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[2]/button[1]").click()
sleep(1)
#scroll down
driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)/8);")
#telefonla ara
telefon=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/div[2]/div/a")
telefon.click()
#Bilgisayar uzerinden gerceklestirdigimiz icin arama yapamayacagimizdan burada biraktim



#---------------->AFTER<------------------#
driver.delete_all_cookies()
# driver.quit()


