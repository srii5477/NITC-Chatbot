from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
import time

options = Options()
options.headless = False  
options.add_argument("--window-size=1920,1200")

URL = "https://nitc.ac.in/news-and-events"  

DRIVER_PATH = "C:\\Users\\sride\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

driver = webdriver.Chrome(options=options)

driver.get(URL)


content = driver.find_elements(By.TAG_NAME, 'a')

for i in content:
    print(i.text)

driver.quit()