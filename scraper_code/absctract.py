from abc import ABC, abstractmethod
import logging
import numpy as np
from pathlib import Path

from bs4 import BeautifulSoup
import pandas as pd
from newspaper import Article


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
    
    def gets_html(self, url):
        article = Article(url)
        article.download()
        article.parse()
        soup = BeautifulSoup(article.html, 'html.parser')
        return soup
    
    @abstractmethod
    def get_introduction(self, soup):
        pass
    
    @abstractmethod
    def get_ingredients(self, soup):
        pass
    
    @abstractmethod
    def gets_steps(self, soup):
        pass
    
    def get_title(self, article):
        return article.title
    
    @abstractmethod
    def get_votes(self, soup):
        pass
    
    def main(self):
        links_gen = self.links_path.glob("*.txt")
        for links_batch in links_gen:
            logging.info(f":star: Processing {links_batch}")
            links = np.loadtxt(fname=links_batch, dtype=str).tolist()
            errors, values = self.gets_batch(links)
            file_save = self.scrapper_directory/links_batch.name.replace(".txt", ".csv")
            pd.DataFrame(values).to_csv(file_save, index=False)
            self.scrapper_directory/"erros.txt".open("a").write("\n".join(errors))
            logging.info(f":white_check_mark: Done {links_batch}")
            links_batch.rename(self.completed_directory/links_batch)
            
            
        
    def gets_batch(self, links):
        values = []
        errors = []
        for url in links:
            try:
                soup = self.gets_html(url)
                title = self.get_title(soup)
                order = self.gets_steps(soup)
                intro = self.get_introduction(soup)
                votes = self.get_votes(soup)
                ingredients = self.get_ingredients(soup)
                url = url
                info = {
                    "title": title,
                    "order": order,
                    "intro": intro,
                    "votes": votes,
                    "ingredients": ingredients,
                    "url": url
                }
                values.append(info)
            except AttributeError:
                logging.error(f"\t :angry: Error in {url}")
                errors.append(url)
            logging.info(f"\t :smiley: {url} done")
            
        return values, errors
            
        
    
    
    