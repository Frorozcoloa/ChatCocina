from pathlib import Path

from scraper_code.nestle.scrapper import NestleScrapper




    

if __name__ == "__main__":
       host = "https://www.recetasnestle.com.co"
       url_formart = url = "https://www.recetasnestle.com.co/api/srh-recipe-category/{}?page={}&order=latest"
       categories = ["658580", "658586", "658581", "658585", "660796", "660765"]
       NestleScrapper(url_formart, host, categories).main()

