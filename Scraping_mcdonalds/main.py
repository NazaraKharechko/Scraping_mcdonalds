from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json

url = 'https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html'
res = []

class SpanScraper:
    """Цей клас робить основний запит на сайт з меню мака і витягує всі силки на смаколики і зберігає в файлі,
                з якого ми потім діствєм весь опис"""
    def __init__(self, url):
        self.url = url

    def scrape(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        time.sleep(4)
        html_code = driver.page_source
        soup = BeautifulSoup(html_code, 'html.parser')

        # Знайти всі теги 'a' на смаколики
        span_elements = soup.find_all('a', {'class': 'cmp-category__item-link'})
        spans_href = [span.get('href') for span in span_elements]
        for i in spans_href:
            res.append('https://www.mcdonalds.com/' + i)
        print(len(res))
        print(res)
        driver.quit()

        # Запис в файл всіх посилань на меню мака
        # with open('links.json', 'w') as f:
        #     json.dump(res, f)
        return spans_href


if __name__ == "__main__":
    scraper = SpanScraper(url)
    spans_text = scraper.scrape()

