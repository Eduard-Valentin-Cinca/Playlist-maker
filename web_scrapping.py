from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.beatport.com/top-100')
playlist = driver.find_elements(By.CLASS_NAME, 'sc-d187b421-4.bHvdSK')
for t in playlist:
    print(t.text)
