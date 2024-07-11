from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

browser = webdriver.Chrome()

idName = "0555555555"
pw = "uctrs9.21"
url = "https://twitter.com/"

browser.get(url)
time.sleep(2)

giris = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                         "//*[@id='react-root']/div/"
                                                                         "div/div[2]/main/div/div/div[1]/div/"
                                                                         "div/div[3]/div[5]/a/div/span/span")))
giris.click()

username = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                            "//*[@id='layers']/div[2]/div/div/div/div/"
                                                                            "div/div[2]/div[2]/div/div/div[2]/div[2]/"
                                                                            "div/div/div/div[5]/label/div/div[2]/div/input")))
username.send_keys(idName)

ileri = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                         "//*[@id='layers']/div[2]/div/div/div/div/div/"
                                                                         "div[2]/div[2]/div/div/div[2]/div[2]/div/div/"
                                                                         "div/div[6]/div/span/span")))
ileri.click()

password = (WebDriverWait(browser, 10)
            .until(ec.presence_of_element_located((By.XPATH,
                                                   "//*[@id='layers']/div[2]/div/div/div/div/"
                                                   "div/div[2]/div[2]/div/div/div[2]/div[2]/"
                                                   "div[1]/div/div/div[2]/div/label/div/div[2]/div[1]/input"))))
password.send_keys(pw)

giris2 = (WebDriverWait(browser, 10)
          .until(ec.presence_of_element_located((By.XPATH,
                                                 "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/"
                                                 "div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span"))))
giris2.click()

searchArea = (WebDriverWait(browser, 10)
              .until(ec.presence_of_element_located((By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/"
                                                               "div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/"
                                                               "div[1]/div/div/div/label/div[2]/div/input"))))

searchArea.send_keys("#yazilim")
searchArea.send_keys(Keys.ENTER)

lenOfPage = browser.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = False
while not match:
    lastCount = lenOfPage
    time.sleep(2)
    lenOfPage = browser.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match = True

time.sleep(3)

elements = (WebDriverWait(browser, 20)
            ).until(ec.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                         ".css-1rynq56.r-8akbws.r-krxsd3.r-dnmrzs.r-1udh08x.r-bcqeeo.r-qvutc0.r-37j5jr.r-a023e6.r-rjixqe.r-16dba41.r-bnwqim")))

for i in elements:
    print("- - - - - -  - - - - - - - - - - - -  - - - - -  - - - - -  - - - - - ")
    print(i.text)

time.sleep(5)
browser.close()
