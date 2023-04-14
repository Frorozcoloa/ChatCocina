from scraper_code.abstract import ScrapperLinks
from newspaper import Article
from pathlib import Path

class Recetas(ScrapperLinks):
    host = "https://www.recetas.com/p"

    UNIQUE_LINK =[
        "{}/recetas-ucranianas/",
        "{}/recetas-serbias/",
        "{}/recetas-lituanas/",
        "{}/recetas-islandesas/"
        "{}/recetas-georgia/",
        "{}/recetas-euskadi/",
        "{}/recetas-eslovenas/",
        "{}/recetas-guatemaltecas/",
        "{}/recetas-paraguayas/",
        "{}/recetas-dominicanas/"
        "{}/recetas-canadienses/",
        "{}/recetas-salvadorenas/",
        "{}/recetas-hondureas/",
        "{}/recetas-cubanas/",
        "{}/recetas-jamaicanas/",
        "{}/recetas-panameas/",
        "{}/recetas-afganistanies/",
        "{}/recetas-armenia/",
        "{}/recetas-coreanas-sur/",
        "{}/recetas-sirias/",
        "{}/recetas-iranies/",
        "{}/recetas-chipre/",
        "{}/recetas-vietnam/",
        "{}/recetas-argelinas/",
        "{}/recetas-filipinas/",
        "{}/recetas-taiwn/",
        "{}/recetas-nueva-zelanda/"
    ]
    def __init__(self):
        directory = Dataset = Path(__file__).parent.parent.parent / "Datasets"/"Links"
        super(Recetas, self).__init__("Recetas", directory)
    
    def __get_links(self, url):
        soup = self.get_soup(url)
        links = soup.find_all("div", {"class": "show_entry_title"})
        links = [link.find("a")["href"] for link in links]
        return links

    def main(self):
        self.unique_links()

    def unique_links(self):
        save_aa = []
        for link in self.UNIQUE_LINK:
            url = link.format(self.host)
            recetas = self.__get_links(url)
            save_aa.append(recetas)
        self.save_links(save_aa, "unique")

    def get_links(self):
        for info_link in self.info_links:
            values = []
            for page in range(1, info_link["last_page"]+1):
                url = info_link["url_format"].format(self.host, page)
                links = self.__get_links(url)
                values += links
            self.save_batch_links(values, info_link["name"])