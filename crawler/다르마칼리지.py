from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import glob, textract

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)

if __name__=="__main__":
    files = glob.glob("data/다르마칼리지/pdf/*.pdf")
    text_list = []
    for file in files:
        text = textract.process(file).decode('utf-8')
        text_list.append(text)

    idx = 1

    for text in text_list:
        f = open("data/다르마칼리지/csv/data" + str(idx) +".csv", 'w', newline='')
        idx = idx + 1
        wr = csv.writer(f)

        wr.writerow(["text"])
        for line in text:
            wr.writerow([line])
        f.close()