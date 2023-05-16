from scraper_code.abstract import LINKS, ScrapperLinks
from scraper_code.scrapper import Scrapper
from newspaper import Article
from pathlib import Path

from bs4 import BeautifulSoup

class LinksOkdiario(ScrapperLinks):
    def __init__(self, name="okdiario"):
        super().__init__(name)
        self.utl_format = "https://okdiario.com/recetas/ultimas-noticias/{}"
    
    def get_links(self, page=None):
        url = self.utl_format.format(page)
        soup = self.get_soup(url)
        links = soup.find("section", class_="content").find_all("a", class_="article-link")
        links = [i.get("href") for i in links]
        return links
    
    def main(self):
        for i in range(1, 314):
            links = self.get_links(i)
            self.save_batch_links(links, f"page_{i}")
            print(f"Done {i}")
    

class Okdiario(Scrapper):
    def __init__(self, name = "okdiario"):
        super().__init__(name)
    

    def get_ingrediants(self, html):
        soup = BeautifulSoup(html, "html.parser")
        porcion = soup.find("div", class_="entry-content").find("div").find_all("li", recursive=False)
        porcion = [i.text for i in porcion]
        text = ". ".join(porcion)
        return text
    
    def get_steps(self, html):
        soup = BeautifulSoup(html, "html.parser")
        porcion = soup.find("div", class_="entry-content").find("ol").find_all("li")
        porcion = [i.text for i in porcion]
        text = ". ".join(porcion)
        return text