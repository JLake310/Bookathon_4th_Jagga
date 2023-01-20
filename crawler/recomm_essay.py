from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from tqdm import tqdm
from selenium.webdriver.common.by import By

class EssayClawer:
    def __init__(self) -> None:
        pass
    
    def crawl(self):
        url = "https://jaemisupil.com/index.php?mid=recommend_articles&page=1"

        print('=====Initialize Drive=====')
        driver = self.initDrive(url)

        print('=====Start parsing=====')
        data = self.parse(driver)

        # print('data 수:', len(data))
        print('====End====')

        # print('save to csv')
        # data.to_csv("./netflix.csv", encoding='utf-8', index=False)

        return data


    def initDrive(self, url):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disabled-popup-blocking')
        chrome_options.add_argument('--headless') #내부 창을 띄울 수 없으므로 설정
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome('/Users/yejin/Desktop/ /4-1/AI_Project/TeamProject/chromedriver') # Mac M1
        driver.get(url)

        return driver

    def parse(self, driver):
        for i in range(33, 63):
            url = f"https://jaemisupil.com/index.php?mid=recommend_articles&page={i}"
            driver.get(url)

            for j in tqdm(range(3, 23), desc=f"{i}page"):
                try:
                    ul = driver.find_element(By.XPATH, f'//*[@id="body_container"]/div/div[2]/div[2]/form/table/tbody/tr[{j}]')
                except:
                    pass
                else:
                    a = ul.find_element(By.TAG_NAME, 'a')
                    href = a.get_attribute('href')
                    
                    driver.get(href) #해당 페이지 들가기
                    div = driver.find_element(By.CLASS_NAME, "originalContent")
                    data = div.text.split('. ')

                    data = pd.DataFrame({"text":data})
                    print(f'save! {((i-1)*20)+(j-2)}')
                    data.to_csv(f"./추천수필/data{((i-1)*20)+(j-2)}.csv", encoding='utf-8', index=False)
        
if __name__ == '__main__':
    mc = EssayClawer()
    mc.crawl()