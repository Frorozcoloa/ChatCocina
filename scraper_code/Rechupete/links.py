from scraper_code.abstract import ScrapperLinks
from newspaper import Article

class Rechupetes(ScrapperLinks):
    def __init__(self, name, url_format, last_page, start_page=1):
        super(Rechupetes, self).__init__(name)
        self.url_format = url_format
        self.last_page = last_page
        self.start_page = start_page
        
    def main(self):
        for page in range(self.start_page,self.last_page):
            links = self.get_links(page)
            self.save_batch_links(links, f"Rechupete_{page}")
    
    def __get_links(self, soup):
        archive = soup.find('div', id='archive')
        posts = archive.find_all('div', class_='post')
        links = [post.find('a')['href'] for post in posts]
        return links
        
        
    def get_links(self, page):
        url = self.url_format.format(page)
        soup = self.get_soup(url)
        links = self.__get_links(soup)
        return links
        
    