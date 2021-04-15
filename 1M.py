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
driver.maximize_window()

try:
    kapat_kampanya = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "modal__close"))
    )
finally:
    kapat_kampanya.click()



#---------------->TEST<------------------#

driver.get(driver.current_url+"satilik")

#filtrele Dropdown
try:
    dropdown = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[3]/div/button[2]"))
    )
finally:
    dropdown.click()
#cerez kapat
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/section[1]/div[2]/select").click()
#izmir sec
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/section[1]/div[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/section[1]/div[2]/select/option[4]").click()
#bornova sec
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/section[1]/section[1]/div[1]").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/section[1]/section[1]/div[2]/div[2]/div[2]/li[7]/label/input").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/section[1]/section[1]/div[2]/button").click()
#scroll down
driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)/8);")
#isyeri
sleep(1)
driver.find_element_by_css_selector("#app > div.listing-main-wrapper > div.listing > div.listing-wrapper.filter-wrapper > div > div.wrapper > div:nth-child(4) > div > ul > li:nth-child(2)").click()
#fiyat
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/section[2]/div/div[1]/input").send_keys("100000")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/section[2]/div/div[2]/input").send_keys("2000000")
#scroll
driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)/2);")
#binayasi
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/section[5]/section/div").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/section[5]/section/div[2]/div[2]/ul/li[1]").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/section[5]/section/div[2]/div[2]/ul/li[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/section[5]/section/div[2]/div[2]/ul/li[3]").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/section[5]/section/div[2]/button").click()
#sonuclari goster
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[2]/button[1]").click()
sleep(1)
#filtrele
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[3]/div/button[2]").click()



#---------------->AFTER<------------------#

# kontrol
if(driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/div/div/div/div/div[1]/div/div/p").text=="6-10"
and driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/div/div/div/div/div[2]/div/div/p").text=="1-5"
and driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/div/div/div/div/div[3]/div/div/p").text=="Sıfır Bina"
):
    print("\n\nKontrol edildi.Dogru filtrelenmis...\n\n")
else:
    print("\n\nFiltrelemede hata yapilmis...\n\n")

driver.delete_all_cookies()
# driver.quit()

