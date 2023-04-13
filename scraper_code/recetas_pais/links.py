from scraper_code.abstract import ScrapperLinks
from newspaper import Article
from pathlib import Path

class Recetas(ScrapperLinks):
    host = "https://www.recetas.com/p"
    info_links =[
        {
            "url_format": "{}/recetas-alemanas/{}/",
            "name":"alemania",
            "last_page": 10
        },
        {
            "url_format": "{}/recetas-dinamarca/{}/",
            "name": "dinamarca",
            "last_page": 2
        },
        {
            "url_format": "{}/recetas-espanolas/{}/",
            "name": "espana",
            "last_page": 109
        },
        {
            "url_format": "{}/recetas-finlandesas/{}/",
            "name": "finlandia",
            "last_page": 2
        },
        {
            "url_format": "{}/recetas-griegas/{}/",
            "name": "grecia",
            "last_page": 8
        },
        {
            "url_format": "{}/recetas-inglaterra/{}/",
            "name": "inglaterra",
            "last_page": 6
        },
        {
            "url_format": "{}/recetas-italianas/{}/",
            "name": "italia",
            "last_page": 84
        },
        {
            "url_format": "{}/recetas-paises-bajos/{}/",
            "name": "paises_bajos",
            "last_page": 1
        },
        {
            "url_format": "{}/recetas-inglesas/{}/",
            "name": "reino_unido",
            "last_page": 2
        },
        {
            "url_format": "{}/recetas-rumania/{}/",
            "name": "rumania",
            "last_page": 1
        },
        {
            "url_format": "{}/recetas-suecas/{}/",
            "name": "suecia",
            "last_page": 2
        },
        {
            "url_format": "{}/recetas-austriacas/{}/",
            "name": "austria",
            "last_page": 4
        },
        {
            "url_format": "{}/recetas-bulgaria/{}/",
            "name": "bulgaria",
            "last_page": 1
        },
        {
            "url_format": "{}/recetas-eslovacas/{}/",
            "name": "eslovaquia",
            "last_page": 1
        },
        {
            "url_format": "{}/recetas-estonias/{}/",
            "name": "estonia",
            "last_page": 1
        },
        {
            "url_format": "{}/recetas-francesas/{}/",
            "name": "francia",
            "last_page": 57
        },
        {
            "url_format": "{}/recetas-holandesas/{}/",
            "name": "holanda",
            "last_page": 1
        },
        {
            "url_format": "{}/recetas-irlandesas/{}/",
            "name": "irlanda",
            "last_page": 2
        },
        {
            "url_format": "{}/recetas-letonas/{}/",
            "name": "letonia",
            "last_page": 1
        },
        {
            "url_format": "{}/recetas-malta/{}/",
            "name": "malta",
            "last_page": 1
        },
        {
            "url_format": "{}/recetas-polonia/{}/",
            "name": "polonia",
            "last_page": 1
        },
        {
            "url_format": "{}/recetas-checas/{}/",
            "name": "republica_checa",
            "last_page": 1
        },
        {
            "url_format": "{}/recetas-rusas/{}/",
            "name": "rusia",
            "last_page": 5
        },
        {
            "url_format": "{}/recetas-suizas/{}/",
            "name": "suiza",
            "last_page": 4
        },
        {
            "url_format": "{}/recetas-belgica/{}/",
            "name": "belgica",
            "last_page": 1
        },
        {
            "url_format": "{}/recetas-portuguesas/{}/",
            "name": "portugal",
            "last_page": 2
        },
        {
            "url_format": "{}/recetas-noruegas/{}/",
            "name": "noruega",
            "last_page": 2
        },
        {
            "url_format": "{}/recetas-hungaras/{}/",
            "name": "hungria",
            "last_page": 2
        },
        {
            "url_format": "{}/recetas-ecuatorianas/{}/",
            "name": "ecuador",
            "last_page": 2
        },
         {
            "url_format": "{}/recetas-costarricenses/{}/",
            "name": "costa_rica",
            "last_page": 3
        },
         {
            "url_format": "{}/recetas-uruguayas/{}/",
            "name": "uruguay",
            "last_page": 2
        },
         {
            "url_format": "{}/recetas-bolivianas/{}/",
            "name": "bolivia",
            "last_page": 3
        },
         {
            "url_format": "{}/recetas-puertorriquenas/{}/",
            "name": "puerto_rico",
            "last_page": 2
        },
          {
            "url_format": "{}/recetas-venezolanas/{}/",
            "name": "venezuela",
            "last_page": 2
        },
          {
              "url_format": "{}/recetas-americanas/{}/",
              "name": "estados_unidos",
              "last_page": 18
          },
          {
              "url_format": "{}/recetas-chilenas/{}/",
              "name": "chile",
              "last_page": 17
          },
          {
              "url_format": "{}/recetas-argentinas/{}/",
              "name": "argentina",
                "last_page": 139
          },
          {
              "url_format": "{}/recetas-mexicanas/{}/",
              "name": "mexico",
              "last_page": 26
          },
          {
              "url_format": "{}/recetas-colombianas/{}/",
              "name": "colombia",
              "last_page": 18
          },
          {
              "url_format": "{}/recetas-brasilenas/{}/",
              "name": "brasil",
              "last_page": 11
          },
          {
              "url_format": "{}/recetas-japonesas/{}/",
              "name": "japon",
              "last_page": 3
          },
          {
              "url_format": "{}/recetas-arabes/{}/",
              "name": "arabes",
              "last_page": 4
          },
          {
              "url_format": "{}/recetas-egiptas/{}/",
              "name": "egipto",
              "last_page": 2
          },
          {
              "url_format": "{}/recetas-libanesas/{}/",
              "name": "libia",
              "last_page": 2
          },
          {
              "url_format": "{}/recetas-tailandesas/{}/",
              "name": "tailandia",
              "last_page": 2
          },
          {
              "url_format": "{}/recetas-indonesia/{}/",
              "name": "indonesia",
              "last_page": 2
          },
          {
              "url_format": "{}/recetas-israelies/{}/",
              "name": "israel",
              "last_page": 3
          },
          {
              "url_format": "{}/recetas-chinas/{}/",
              "name": "china",
              "last_page": 7
          },
          {
              "url_format": "{}/recetas-indias/{}/",
              "name": "china",
              "last_page": 7
          },
          {
              "url_format": "{}/recetas-australianas/{}/",
              "name": "australia",
              "last_page":3
          }
    ]
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
        self.get_links()
        self.unique_links()

    def unique_links(self):
        save_aa = []
        for link in self.UNIQUE_LINK:
            url = link.format(self.host)
            recetas = self.__get_links(link)
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