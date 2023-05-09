from  scraper_code.scrapper import Scrapper
from bs4 import BeautifulSoup


class BounvierScrapper(Scrapper):
    def __init__(self, name="bounvier"):
        super().__init__(name)
    
    def get_ingrediants(self, html):
        soup = BeautifulSoup(html, "html.parser")
        