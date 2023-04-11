from pathlib import Path

from scraper_code.Rechupete.links import Rechupetes
from scraper_code.scrapper import PequesScrapper


def main():
    dataset = Path("Datasets\Links")
    name = "Rechupete"
    directory = dataset/name
    directory.mkdir(parents=True, exist_ok=True)
    directory_len = len(list(directory.glob("*.txt")))
    rechupetes = Rechupetes(
        name= name,
        url_format="https://www.recetasderechupete.com/todas/recetas/page/{}/",
        last_page=82,
        start_page=directory_len+1
    )
    rechupetes.main()

def main_scrapper():
    scrapper = PequesScrapper("Rechupete")
    scrapper.main()
    

if __name__ == "__main__":
    main_scrapper()
