from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.beatport.com/top-100')
playlist = driver.find_elements(By.CLASS_NAME, 'sc-d187b421-4.bHvdSK')
my_list = []
for t in playlist:
    my_list.append(t.text)


track_names = [(element.split('\n')[0] + ' ' + element.split('\n')[1]) for element in my_list]


