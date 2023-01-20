from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)

if __name__=="__main__":
    for url_num in range(6, 30):
        driver.get(url="https://culture.yeongnam.com/sufeel/contest_result/bbs.php?code=notice&mode=view&idx="+str(url_num))
        data_path = driver.find_element(By.XPATH, '//*[@id="bbs_con"]')
        text = data_path.text.replace("\n", "").split(". ")
        f = open("책사랑 주부수필/data" + str(url_num-5) +".csv", 'w', newline='')
        wr = csv.writer(f)
        
        wr.writerow(["text"])
        for line in text:
            wr.writerow([line])
        f.close()