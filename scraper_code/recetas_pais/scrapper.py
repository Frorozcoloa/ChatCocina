from scraper_code.scrapper import Scrapper


class RecetaPais(Scrapper):
    def __init__(self, name="Recetas"):
        super(RecetaPais, self).__init__(name)
    
    def get_ingrediants(self, text, title):
        try:
            values = text.split("Cómo hacer")
            ingredients = values[0].replace("Ingredientes", "")
            steps = self.get_steps(values[1], title)
            return values
        except IndexError:
            return None, None
    
    def get_steps(self, txt, title):
        text = txt.replace(title, "")
        return txt
    
    def scrapping(self, url):
        info  = self.scraping_default(url)
        text = info.pop("text")
        title = info["title"]
        values= self.get_ingrediants(text, title)
        if values is None:
            return None
        info.pop("html")
        info["ingredients"] = values[0]
        info["steps"] = values[1]
        return info
    