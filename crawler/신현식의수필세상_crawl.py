from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

#2022 첫 수술 작품 누락 계산 실수했음
class WSJCrawler:
    def __init__(self) -> None:
        pass
    
    def crawl(self):
        data = []
        num =0
        for i in range(1,2): #664
            url = f"https://hssin2280.tistory.com/?page={i}" #접속할 페이지 
            base = f"https://hssin2280.tistory.com"
            print('Initialize Drive')
            driver,soup = self.initDrive(url)

            print('Start parsing')
            data, num = self.parse(driver, soup, url, base, num)
            num = num
            print('data 수:', len(data))


            # print('Save to csv')
            # data.to_csv(f"./신현식의 수필세상/csv_data/data{i}.csv", encoding='utf-8-sig', index=False)

            # print('Save to txt')
            # data.to_csv(f'./신현식의 수필세상/txt_data/data{i}.txt', sep="\t", encoding = 'utf-8-sig', index=False)

        # print('data 수:', len(data))

        # print('Save to csv')
        # data.to_csv(f"data{num}.csv", encoding='utf-8-sig', index=False)

        return driver

    def initDrive(self, base_url):
        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_argument('--headless') #내부 창을 띄울 수 없으므로 설정

        chrome_options.add_argument('--no-sandbox')

        chrome_options.add_argument('--disable-dev-shm-usage')

        #### 사용하기 전, 절대경로로 수정해주세요.
        #driver = webdriver.Chrome('/Users/yejin/Yejin_drive/VSC_projects/final-project-level3-nlp-01/src/chromedriver') # Mac M1
        driver = webdriver.Chrome('./신현식의 수필세상/chromedriver.exe') # Window
        driver.get(base_url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        time.sleep(3)

        return driver, soup


    def parse(self, driver, soup, url,base, i):

        a_list = soup.find_all("div", {"class":"post-item"})
        #print(a_list)
        print(url)
        for a in a_list:
            temp = a.find("a")
            writings_link = temp['href']
            #새 페이지
            #print(writings_link) 
            driver.get(base+writings_link)
            print(base+writings_link)
            i = i+1

            writing = driver.find_element(By.CSS_SELECTOR, "#content > div > div.entry-content > div.tt_article_useless_p_margin.contents_style")
            print(writing)
            print(type(writing))
            print(writing.value_of_css_property("data-ke-size").text)
            #writings = [ write for write in writing.split(".")]
            #data = pd.DataFrame({"contents": writing}, index= [0])
            print(i)
            #print('Save to csv')
            #data.to_csv(f"./신현식의 수필세상/data{i}.csv", encoding='utf-8-sig', index=False)
            # print('Save to txt')
            # data.to_csv(f'./신현식의 수필세상/txt_data/data{i}.txt', sep="\t", encoding = 'utf-8-sig', index=False)
            
            

        return 0

        #data = pd.DataFrame({"articles": articles})

        #return data
    
if __name__ == '__main__':
    mc = WSJCrawler()
    mc.crawl()