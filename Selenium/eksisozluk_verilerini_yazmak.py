import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

url = "https://eksisozluk.com/duz-dunya-teorisi--5291800?p="

pageCount = 0
entries = []
entryCount = 0

while pageCount < 10:
    randomPage = random.randint(1, 228)
    newUrl = url + str(randomPage)
    browser.get(newUrl)
    elements = browser.find_elements(By.CSS_SELECTOR, ".content")
    for element in elements:
        entries.append(element.text)
    time.sleep(3)
    pageCount += 1

with open("entries.txt", "w", encoding="UTF-8") as file:
    for entry in entries:
        file.write(str(entryCount+1) + ".\n" + entry + "\n")
        file.write("- - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
        entryCount += 1

browser.close()




