from abc import ABC, abstractmethod
import numpy as np
from pathlib import Path

from bs4 import BeautifulSoup
import pandas as pd
from newspaper import Article, ArticleException

from scraper_code.logging import logging


DATASET = Path(__file__).parent.parent / "Datasets"
LINKS = DATASET/"Links"
SCRAPPER = DATASET/"Scrapper"
COMPLETED = DATASET/"Completed"

class Scrapper(ABC):
    
    def __init__(self, name):
        self.links_path = LINKS / name
        self.scrapper_directory = SCRAPPER / name
        self.completed_directory = COMPLETED / name
        self.scrapper_directory.mkdir(exist_ok=True)
        self.completed_directory.mkdir(exist_ok=True)
    
    @abstractmethod
    def get_ingrediants(self, html):
        pass
    
    @abstractmethod
    def get_steps(self, html):
        pass
    
    def scrapping(self, url):
        article = self.gets_html(url)
        title = article.title
        date = article.publish_date
        url = article.url
        try:
            ingredientes = self.get_ingrediants(article.html)
            steps = self.get_steps(article.html)
            info = {"title": title, "date": date, "url": url, "ingredients": ingredientes, "steps": steps}
            return info
        except AttributeError:
            print(f"\t :angry: Error in {url}")
            return None
    
    def gets_html(self, url):
        article = Article(url, lenguage='es')
        article.download()
        article.parse()
        return article
    
    def main(self):
        links_gen = self.links_path.glob("*.txt")
        
        for links_batch in links_gen:
            print(f":star: Processing {links_batch}")
            links = np.loadtxt(fname=links_batch, dtype=str).tolist()
            try: 
                values, idx = self.gets_batch(links)
            except ArticleException:
                logging.error(f"Error in ")
                continue
            # Prepare datasets
            file_save = self.scrapper_directory/links_batch.name.replace(".txt", ".csv")
            #Save dataset
            pd.DataFrame(values).to_csv(file_save, index=False)
            #Saver errors
            
            print(f":white_check_mark: Done {links_batch}")
            #Cut to completed
            links_save = links[:idx]
            links_dont_save = links[idx+1:]
            links_directory_save = self.completed_directory/links_batch.name
            links_directory_save.open("a").writelines("\n".join(links_save))
            if len(links_dont_save) > 0:
                links_batch.open("w").writelines("\n".join(links_dont_save))
            else:
                links_batch.unlink()
            print(f":white_check_mark: Saved {links_batch}")

    def gets_batch(self, links):
        values = []
        errors = []
        for idx,url in enumerate(links):
            info = self.scrapping(url)
            if info is not None:
                values.append(info)
            else:
                errors.append(url)
        return values, idx
            
        
    
    
class PequesScrapper(Scrapper):
    def __init__(self, name):
        super().__init__(name)
        
    def gets_html(self, url):
        article = Article(url, lenguage='es')
        article.download()
        article.parse()
        return article
    
    def get_ingrediants(self, html):
        soup = BeautifulSoup(html, "html.parser")
        try:
            ingrediants = soup.find("div", {"id": "ingredients"}).find_all("li")
            ingrediants = [i.text for i in ingrediants]
            text = "-".join(ingrediants)
            return text
        except AttributeError:
            return None

    def scrapping(self, url):
        info = self.scraping_default(url)
        if info is None:
            return None
        html = info.pop("html")
        ingredients = self.get_ingrediants(html)
        info["ingredients"] = ingredients
        return info
        