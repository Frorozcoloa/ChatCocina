from scraper_code.abstract import LINKS, ScrapperLinks
from newspaper import Article
from pathlib import Path
from urllib.parse import urlparse

class BounvierLinks(ScrapperLinks):
    def __init__(self, name="bounvier"):
        super().__init__(name)
        self.url_format = "https://www.bonviveur.es/recetas/{}/"
    
    def main(self):
        links_all = []
        for page in range(2,110):
            links = self.get_links(page)
            links_all.extend(links)
            print(f"{page}/109")
            self.save_batch_links(links_all, page)
    
    def get_links(self, page=None):
        url = self.url_format.format(page)
        soup = self.get_soup(url)
        links = soup.find_all("a", {"class": "title"})
        links = [link["href"] for link in links]
        return links