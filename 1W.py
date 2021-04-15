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



            #---------------->SETUP<----------------#

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH, chrome_options=chrome_options) #?Hangi browserda test yapmak istediginle alakali
driver.get("https://www.hurriyetemlak.com")
driver.maximize_window()




            #---------------->TEST<------------------#
#reklam kapat
try:
    kapat_kampanya = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "modal__close"))
    )
finally:
    kapat_kampanya.click()
driver.get(driver.current_url+"satilik")
#cookie kapat
try:
    kapat_cookie = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"#__layout > div > section > p > span"))
    )
finally:
    kapat_cookie.click()
#izmir
try:
    il_dropdown_tikla = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/section[2]/div/section[1]/section[1]/div/div/div/div/div"))
    )
finally:
    il_dropdown_tikla.click()

try:
    izmir_sec = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/section[2]/div/section[1]/section[1]/div/div/div/div/div/div[2]/div/div[1]/ul/li[3]/div"))
    )
finally:
    izmir_sec.click()
#bornova
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
    ilce_input.send_keys("Bornova")

bornova_sec = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/section[2]/div/section[1]/section[2]/div/div/div/div[2]/div/div[1]/ul/li/div")
bornova_sec.click()
ilce_dropdown_tikla.click()
#isyeri
try:
    isyeriSec = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"#listPage > div.list-page-wrapper > div.wrapper.list-wrapper > div > div.left-content > div:nth-child(1) > section.listing-filter > div > section.filter-item-wrap.categoryMainSec > div > ul > li:nth-child(2)"))
    )
finally:
    isyeriSec.click()
sleep(3)
#scroll down
driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)/10);")
#fiyat
try:
    fiyatAltSinir = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/section[2]/div/section[4]/div/div[1]/input"))
    )                                                  
finally:
    fiyatAltSinir.send_keys("100000")
try:
    fiyatUstSinir = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/section[2]/div/section[4]/div/div[2]/input"))
    )
finally:
    fiyatUstSinir.send_keys("2000000")
# bina yasi
try:
    binaYasiDropdown = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/section[2]/div/section[7]/section/div/div/div"))
    )
finally:
    binaYasiDropdown.click()
#0-10
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/section[2]/div/section[7]/section/div/div[2]/div/div/ul/li[1]").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/section[2]/div/section[7]/section/div/div[2]/div/div/ul/li[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/section[2]/div/section[7]/section/div/div[2]/div/div/ul/li[3]").click()
binaYasiDropdown.click()
#ara
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/section[2]/div/section[21]/a[1]").click()



            #---------------->AFTER<------------------#

#---------KONTROL
if(
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/ul/li[1]/span[2]").text=="İzmir"
    and driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/ul/li[2]/span[2]").text=="Bornova"
    and driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/ul/li[3]/span[2]").text=="İşyeri"
    and driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/ul/li[4]/span[2]").text=="100.000 TL - 2.000.000 TL"
    and driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/ul/li[5]/span[2]").text=="Sıfır Bina"
    and driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/ul/span[1]").text=="1-5"
    and driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/ul/span[2]").text=="6-10"
):
    print("Kontrol edildi.Dogru filtrelenmis...")
else:
    print("Filtrelemede hata yapilmis...")
driver.delete_all_cookies()
# driver.quit()




