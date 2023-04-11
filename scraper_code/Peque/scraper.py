from newspaper import Article
from bs4 import BeautifulSoup


from scraper_code.absctract import Scrapper

class ScrapperPeque(Scrapper):
    def __init__(self, name):
        super().__init__(name)
    
    def get_introduction(self, article):
        return article.text
    
    def get_ingredients(self, article):
        text = article.text
        ingredientes = text.slipt("Ingredientes")[-1]
        ingregientes
    
    def gets_steps(self, article):
        return None
    
    def get_votes(self, article):
        return None