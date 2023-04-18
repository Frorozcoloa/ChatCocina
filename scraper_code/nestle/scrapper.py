import requests
import numpy as np
from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd
from newspaper import Article, ArticleException

DATASET = Path(__file__).parent.parent.parent / "Datasets" /"Scrapper"
LINKS = DATASET/"Links"
SCRAPPER = DATASET/"Scrapper"
COMPLETED = DATASET/"Completed"

class NestleScrapper:
    def __init__(self, url_formart, host, categories):
        self.url_formart = url_formart
        self.host = host
        self.categories = categories
        self.dataset = DATASET/"Nestle"
        self.dataset.mkdir(exist_ok=True)
        
    def gets_ingredients(self, soup):
        li = soup.find("div", {"class":"recipeDetail__ingredients"}).find_all("li")
        list_text = [li.text for li in li]
        text = " ".join(list_text)
        text = text.replace("\n", " ").replace("\t", "")
        return text

    def gets_steps(self, soup):
        li = soup.find("div", {"class":"recipeDetail__steps"}).find_all("li")
        list_text = [li.text for li in li]
        text = " ".join(list_text)
        text = text.replace("\n", " ").replace("\t", "")
        return text

    def get_info(self, url):
        url = self.host + url
        art = Article(url, lenguage='es')
        art.download()
        art.parse()
        htlm = art.html
        soup = BeautifulSoup(htlm, "html.parser")
        title = art.title
        ingredients = self.gets_ingredients(soup)
        steps = self.gets_steps(soup)
        info = {
            "url": url,
            "title": title,
            "ingredients": ingredients,
            "steps": steps,
        }
        return info
    
    def main(self):
        for category in self.categories:
            print(f":star: Processing {category}")
            values = []
            i = 0
            while True:
                url = self.url_formart.format(category,i )
                response = requests.get(url)
                if response.ok:
                   data = response.json()
                   results = data.get("results", None)
                   if results is None:
                       break
                   for result in results:
                       url = result["url"]
                       info = self.get_info(url)
                       values += [info]
                       print(f"\t {i} {info['title']}")
                i += 1
            file_save = self.dataset/f"{category}.csv"
            pd.DataFrame(values).to_csv(file_save, index=False)
            print(f":white_check_mark: Done {category}")