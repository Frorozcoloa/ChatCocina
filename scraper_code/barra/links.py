from scraper_code.abstract import ScrapperLinks
from newspaper import Article
from pathlib import Path
from urllib.parse import urlparse


class BarraLinks(ScrapperLinks):
    LINK = "https://ybarraentucocina.com/recetas/page/{}/"
    def __init__(self, name="Barra"):
        directory  = Path(__file__).parent.parent.parent / "Datasets"/"Links"
        super().__init__(name, directory)
    
    def __get_links(self, url):
        soup = self.get_soup(url)
        links = soup.find_all("a", {"class": "slide-image"})
        links = [link["href"] for link in links]
        return links

    def main(self):
        self.get_links()
        
    def get_links(self, page=None):
        total_links = []
        for page in range(1, 138):
            url = self.LINK.format(page)
            links = self.__get_links(url)
            total_links.extend(links)
        self.save_batch_links(total_links, f"links_{page}")