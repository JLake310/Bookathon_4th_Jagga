from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)

if __name__=="__main__":
    for url_num in range (10, 12):
        driver.get(url="https://www.kookje.co.kr/page/nakdonggang/?p=" + str(url_num))
        data_path = driver.find_element(By.XPATH, '//*[@id="picture_con"]/div')
        text = data_path.text.replace("\n", "").split(". ")

        f = open("낙동강/data" + str(url_num) +".csv", 'w', newline='')
        wr = csv.writer(f)

        wr.writerow(["text"])
        for line in text:
            wr.writerow([line])
        f.close()