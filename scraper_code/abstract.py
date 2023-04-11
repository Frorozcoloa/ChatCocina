from abc import ABC, abstractmethod
from pathlib import Path

from bs4 import BeautifulSoup
from newspaper import Article

DATASET = Path(__file__).parent.parent / "Datasets"
LINKS = DATASET/"Links"

class ScrapperLinks(ABC):
    def __init__(self, name, directory=LINKS):
        self.name = name
        self.__directory = directory/name
        

    @abstractmethod
    def get_links(self, page=None):
        pass
    
    @abstractmethod
    def main(self):
        pass
    
    def get_soup(self, url):
        art = Article(url, language='es')
        art.download()
        art.parse()
        soup = BeautifulSoup(art.html, 'html.parser')
        return soup

    
    def save_batch_links(self, links, name):
        links_path = self.__directory / f"{name}.txt"
        with links_path.open(mode='w') as f:
            f.write('\n'.join(links))
        print(f"Links saved in {links_path}")