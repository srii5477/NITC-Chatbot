from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
import time
import csv

options = Options()
options.headless = False  
options.add_argument("--window-size=1920,1200")

URL = "https://nitc.ac.in/news-and-events"  

DRIVER_PATH = "C:\\Users\\sride\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

driver = webdriver.Chrome(options=options)

driver.get(URL)


titles = driver.find_elements(By.CLASS_NAME, 'xc-title')
dates = driver.find_elements(By.CLASS_NAME, 'xc-date')

title_text = []
dates_text = []

for i in titles:
    print(i.text)
    title_text.append(i.text)
    
for i in dates:
    print(i.text)
    dates_text.append(i.text)

data = list(zip(title_text, dates_text))
with open("data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Date"])  # Write the header
        writer.writerows(data)  # Write the data rows

driver.quit()