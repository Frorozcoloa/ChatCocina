from  scraper_code.scrapper import Scrapper
from bs4 import BeautifulSoup

class BarraScrapper(Scrapper):
    def __init__(self, name="Barra"):
        super().__init__(name)
    
    def get_ingrediants(self, html):
        soup = BeautifulSoup(html, "html.parser")
        ingredients = soup.find("ul", {"class": "recipe-list"}).text
        ingredients = ingredients.replace("\n", " ")
        return ingredients
    
    def get_steps(self, html):
        soup = BeautifulSoup(html, "html.parser")
        steps = soup.find("div", {"class": "step-contain"}).text
        steps = steps.replace("\n", " ")
        return steps
    
    