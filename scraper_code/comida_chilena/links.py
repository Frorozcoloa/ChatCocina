from scraper_code.abstract import ScrapperLinks
from newspaper import Article
from pathlib import Path
from urllib.parse import urlparse

class Chilena(ScrapperLinks):
    LINK = "https://www.gourmet.cl/recetas/page/{}/"
    def __init__(self, name="Chilena"):
        directory  = Path(__file__).parent.parent.parent / "Datasets"/"Links"
        super().__init__(name, directory)
    
    def __get_links(self, url):
        soup = self.get_soup(url)
        links = soup.find_all("div", {"class": "link text-center"})
        links = [link.find("a")["href"] for link in links]
        links = list(filter(lambda x: urlparse(x).netloc == "www.gourmet.cl", links))
        return links
    def main(self):
        self.get_links()
        
    def get_links(self, page=None):
        for page in range(1, 59):
            url = self.LINK.format(page)
            links = self.__get_links(url)
            self.save_batch_links(links, f"links_{page}")