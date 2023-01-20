from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)

if __name__=="__main__":
    url_num = [93, 92, 91, 90, 89, 81, 71, 70, 65, 61, 54, 28, 22, 18, 11, 7, 2]
    idx = 1
    for url in url_num:
        driver.get(url="https://bookclub.dongsuh.co.kr/05_literature/01_together_literature_view.asp?work_code="+str(url))
        data_path = driver.find_element(By.XPATH, '//*[@id="contentsWrap"]/div[2]/div/div/div/div[1]/div/p')
        text = data_path.text.replace("\n", "").split(". ")
        f = open("동서식품/data" + str(idx) +".csv", 'w', newline='')
        idx = idx + 1
        wr = csv.writer(f)
        wr.writerow(["text"])
        for line in text:
            wr.writerow([line])
        f.close()