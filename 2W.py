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

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH, chrome_options=chrome_options) #?Hangi browserda test yapmak istediginle alakali
url="https://www.hurriyetemlak.com"
driver.get(url)
driver.maximize_window()
try:
    kapat_kampanya = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "modal__close"))
    )
finally:
    kapat_kampanya.click()



            #---------------->TEST<------------------#

driver.get(driver.current_url+"kiralik")
try:
    kapat_cookie = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"#__layout > div > section > p > span"))
    )
finally:
    kapat_cookie.click()
#ankara
try:
    il_dropdown_tikla = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/section[2]/div/section[1]/section[1]/div/div/div/div/div"))
    )
finally:
    il_dropdown_tikla.click()

try:
    ankara_sec = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/section[2]/div/section[1]/section[1]/div/div/div/div/div/div[2]/div/div[1]/ul/li[2]/div"))
    )
finally:
    ankara_sec.click()
#cankaya
try:
    ilce_dropdown_tikla = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/section[2]/div/section[1]/section[2]/div/div/div"))
    )
finally:
    ilce_dropdown_tikla.click()

try:
    ilce_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/section[2]/div/section[1]/section[2]/div/div/div/div[2]/input"))
    )
finally:
    ilce_input.send_keys("Çankaya")

cankaya_sec = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/section[2]/div/section[1]/section[2]/div/div/div/div[2]/div/div[1]/ul/li/div")
cankaya_sec.click()
ilce_dropdown_tikla.click()
#scroll down
driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)/10);")
#2+1 
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/section[2]/div/section[6]/section/div/div").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/section[2]/div/section[6]/section/div/div[2]/div/div/ul/li[3]").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/section[2]/div/section[6]/section/div/div").click()
#scroll down
driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)/4);")
# site icerisinde
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/section[2]/div/section[16]/label/div[2]").click()
#ara
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/section[2]/div/section[22]/a[1]").click()
sleep(1)
#scroll down
driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)/11);")
#3.ilani sec
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div[4]").click()
#scroll down
driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)/10);")
sleep(3)
#teledon numarasi islemleri
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section[3]/div/div[2]/div/section/div/div[2]/button").click()
telefon = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section[3]/div/div[2]/div/section/div/div[2]/div/ul/li/a").text
           
           
           
            #---------------->AFTER<------------------#

print("\n\nTelefon numarasi 'telefon' degiskenine alindi = "+telefon+ "\n\n")
driver.delete_all_cookies()
# driver.quit()


