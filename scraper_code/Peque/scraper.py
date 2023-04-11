from newspaper import Article
from bs4 import BeautifulSoup


from scraper_code.absctract import Scrapper

class ScrapperPeque(Scrapper):
    def __init__(self, name):
        super().__init__(name)
    
    def get_introduction(self, soup):
        entry = soup.find("div", {"class": "entry"}).find_all("p")
        intro = [p.text for p in entry]
        intro = " ".join(intro)
        return intro
    
    def get_ingredients(self, soup):
        ingredients =  soup.find_all("li", {"class": "ingredientes"})
        ingredients = [i.text for i in ingredients]
        ingredients = " ".join(ingredients)
        return ingredients
    
    def gets_steps(self, soup):
        steps = soup.find_all("li", {"class": "instrucciones_pasos"})
        steps = [s.text for s in steps]
        steps = " ".join(steps)
        return steps
    
    def get_votes(self, soup):
        return None