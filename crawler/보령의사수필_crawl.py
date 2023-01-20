from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

#2022 첫 수술 작품 누락 계산 실수했음
class WSJCrawler:
    def __init__(self) -> None:
        pass
    
    def crawl(self):
        data = []
 
        for i in range(2005,2006):

            url = f"https://pharm.boryung.co.kr/contribution/essay.do?year={i}"
            print('Initialize Drive')
            driver = self.initDrive(url)

            print('Start parsing')
            data = self.parse(driver)

            print('data 수:', len(data))

            print('Save to csv')
            data.to_csv(f"./보령의사/csv_data/data{i-2004}.csv", encoding='utf-8-sig', index=False)

            print('Save to txt')
            data.to_csv(f'./보령의사/txt_data/data{i-2004}.txt', sep="\t", encoding = 'utf-8-sig', index=False)

        return driver

    def initDrive(self, base_url):
        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_argument('--headless') #내부 창을 띄울 수 없으므로 설정

        chrome_options.add_argument('--no-sandbox')

        chrome_options.add_argument('--disable-dev-shm-usage')

        #### 사용하기 전, 절대경로로 수정해주세요.
        #driver = webdriver.Chrome('/Users/yejin/Yejin_drive/VSC_projects/final-project-level3-nlp-01/src/chromedriver') # Mac M1
        driver = webdriver.Chrome('./보령의사/chromedriver.exe') # Window
        driver.get(base_url)
        time.sleep(3)

        return driver

    def parse(self, driver):
        #articles = []

        #div:nth-child(여기 숫자 바꾸기로 진행)
        medal_link = driver.find_element(By.CSS_SELECTOR, "#container > div > div > div.section.mt0 > div > div:nth-child(1) > div.info > p > a")
        medal_link.click()
        title = driver.find_element(By.CSS_SELECTOR, "#container > div > div > div:nth-child(5) > div.listView > div.listTitle > p > span").text
        article = driver.find_element(By.CSS_SELECTOR, "#container > div > div > div:nth-child(5) > div.listView > div.editorTexts").text
        # articles = [sentence for sentence in article.split(".")]
        print(article)
        print(title)
        data = pd.DataFrame({"contents": article}, index= [0])

        return data
    
if __name__ == '__main__':
    mc = WSJCrawler()
    mc.crawl()