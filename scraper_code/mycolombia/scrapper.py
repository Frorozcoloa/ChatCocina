from  scraper_code.scrapper import Scrapper
from bs4 import BeautifulSoup

class MyColomian(Scrapper):
    def __init__(self):
        name = "mycolombianrecipes"
        super().__init__(name)
    
    def get_ingrediants(self, html):
        soup = BeautifulSoup(html, "html.parser")
        porcion = soup.find_all("li", {"class": "wprm-recipe-ingredient"})
        porcion = [i.text for i in porcion]
        text = "\n".join(porcion)
        return text
    
    def get_steps(self, html):
        soup = BeautifulSoup(html, "html.parser")
        soup = soup.find("ul", {"class": "wprm-recipe-instructions"}).find_all("li")
        steps = [i.text for i in soup]
        steps = "\n".join(steps)
        return steps
    
    def scrapping(self, url):
        article = self.gets_html(url)
        title = article.title
        date = article.publish_date
        url = article.url
        try:
            ingredientes = self.get_ingrediants(article.html)
            steps = self.get_steps(article.html)
            info = {"title": title, "date": date, "url": url, "ingredients": ingredientes, "steps": steps}
            return info
        except AttributeError:
            print(f"\t :angry: Error in {url}")
            return None
            
        
        