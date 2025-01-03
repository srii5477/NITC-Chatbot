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

# URL = "https://nitc.ac.in/news-and-events"  
URL = "https://nitc.ac.in/department/electronics-amp-communication-engineering"

DRIVER_PATH = "C:\\Users\\sride\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

driver = webdriver.Chrome(options=options)

driver.get(URL)


# titles = driver.find_elements(By.CLASS_NAME, 'xc-title')
# dates = driver.find_elements(By.CLASS_NAME, 'xc-date')

# title_text = []
# dates_text = []

# for i in titles:
#     print(i.text)
#     title_text.append(i.text)
    
# for i in dates:
#     print(i.text)
#     dates_text.append(i.text)

# data = list(zip(title_text, dates_text))
# with open("news_events.csv", "w", newline="", encoding="utf-8") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Title", "Date"]) 
#         writer.writerows(data)  

# links = driver.find_elements(By.CLASS_NAME, 'xc-footer-links')
# departments = []
# for i in links:
#     print(i.text)
#     departments.append(i.text)

# departments = [item.replace(",", "") for item in departments]
# departments = [item.replace("\"", "") for item in departments]
# with open("depts.csv", "w", newline="", encoding="utf-8") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Title"])  
#         for item in departments:
#             writer.writerow([item])
# cse = driver.find_elements(By.XPATH, "//div[@class='xc-department-content']//p")
# cse_content = []
# for i in cse:
#     print(i.text)
#     cse_content.append(i.text)
# with open("cse.csv", "w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Description of the CSE Department"])  
#     for item in cse_content:
#         writer.writerow([item])
ece = driver.find_elements(By.XPATH, "//div[@class='xc-department-content']//p")
ece_content = []
for i in ece:
    print(i.text)
    ece_content.append(i.text)
with open("ece.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Description of the ECE Department"])  
    for item in ece_content:
        writer.writerow([item])
driver.quit()