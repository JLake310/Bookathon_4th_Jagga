from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)

if __name__=="__main__":
    for url_num in range(14, 51):
        driver.get(url="https://teen.munjang.or.kr/archives/category/write/life/page/"+str(url_num))
        cnt = len(driver.find_elements(By.CLASS_NAME, 'post_title'))
        
        for i in range(0, cnt):
            driver.find_elements(By.CLASS_NAME, 'post_title')[i].find_element(By.TAG_NAME, 'a').click()
            res = driver.find_element(By.TAG_NAME, 'article').text
            res = res.replace("\n", "").split(". ")
            
            f = open("data/문학광장/data" + str(url_num) + "_"+str(i) +".csv", 'w', newline='')
            wr = csv.writer(f)

            wr.writerow(["text"])
            for line in res:
                wr.writerow([line])
            f.close()
            
            driver.back()