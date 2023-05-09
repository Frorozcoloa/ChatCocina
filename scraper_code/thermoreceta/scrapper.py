from  scraper_code.scrapper import Scrapper
from bs4 import BeautifulSoup


class ThermoScrapper(Scrapper):
    def __init__(self, name = "thermorecetas"):
        super().__init__(name)
    
    def get_ingrediants(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        ingrendients = soup.find("div", class_="abn-recipes-ingredients").text
        text = ingrendients.replace("\n", "")
        return text
    
    def get_steps(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        steps = soup.find("div", class_="abn-recipes-instructions").text
        text = steps.replace("\n", "")
        return text
    
        