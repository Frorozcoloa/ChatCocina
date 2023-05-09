from  scraper_code.scrapper import Scrapper
from bs4 import BeautifulSoup


class ChilenaScrapper(Scrapper):
    def __init__(self, name="Chilena"):
        super().__init__(name)
        
    def get_ingrediants(self, html):
        soup = BeautifulSoup(html, "html.parser")
        ingredients = soup.find("div", {"class": "izquierda"}).find_all("li")
        text = [ingredient.text for ingredient in ingredients]
        text = " ".join(text)
        text = text.replace("\n", " ")
        return text
    
    def get_steps(self, html):
        soup = BeautifulSoup(html, "html.parser")
        steps = soup.find("div", {"class": "derecha"}).find_all("li")
        text = [step.text for step in steps]
        text = " ".join(text)
        text = text.replace("\n", " ")
        return text
    
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