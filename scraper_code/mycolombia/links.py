from scraper_code.abstract import ScrapperLinks
from newspaper import Article
from pathlib import Path

class MyColombia(ScrapperLinks):
    link_info =[
        {
            "url_format": "https://www.mycolombianrecipes.com/es/recetas/platos-principales/page/{}/",
            "name":"PLATOS_PRINCIPALES",
            "last_page": 22
        },
        {
            "url_format": "https://www.mycolombianrecipes.com/es/recetas/acompanamientos/page/{}/",
            "name": "ACOMPAÑAMIENTOS",
            "last_page": 7
        },
        {
            "url_format": "https://www.mycolombianrecipes.com/es/recetas/entradas-y-bocaditos/page/{}/",
            "name": "ENTRADAS_Y_BOCADITOS",
            "last_page": 11
        },
        {
            "url_format": "https://www.mycolombianrecipes.com/es/recetas/ensaladas/page/{}/",
            "name": "ENSALADAS",
            "last_page": 2
        },
        {
            "url_format": "https://www.mycolombianrecipes.com/es/recetas/postres/page/{}/",
            "name": "POSTRES",
            "last_page": 8
        },
        {
            "url_format": "https://www.mycolombianrecipes.com/es/recetas/desayunos-y-brunch/page/{}/",
            "name": "DESAYUNOS_Y_BRUNCH",
            "last_page": 6
        },
        {
            "url_format": "https://www.mycolombianrecipes.com/es/recetas/bebidas/page/{}/",
            "name": "BEBIDAS",
            "last_page": 6
        },
        {
            "url_format": "https://www.mycolombianrecipes.com/es/recetas/pan-y-tortas/page/{}/",
            "name": "PAN_Y_TORTAS",
            "last_page": 4
        },
        {
            "url_format": "https://www.mycolombianrecipes.com/es/recetas/salsas-y-condimentos/page/{}/",
            "name": "SALSAS_Y_CONDIMENTOS",
            "last_page": 2
        }
    ]
    def __init__(self):
        directory = Dataset = Path(__file__).parent.parent.parent / "Datasets"/"Links"
        super(MyColombia, self).__init__("mycolombianrecipes", directory)
    
    def __get_links(self, url):
        soup = self.get_soup(url)
        links = soup.find_all("a", {"class": "entry-title-link"})
        links = [link["href"] for link in links]
        return links

    def get_links(self):
        links_all = []
        for infos in self.link_info:
            last_page = infos["last_page"]
            url_format = infos["url_format"]
            name = infos["name"]
            for page in range(1, last_page+1):
                url = url_format.format(page)
                links = self.__get_links(url)
                links_all += links
        self.save_batch_links(links_all, "all_links")
    
    def main(self):
        self.get_links()
        print("Done!")
            