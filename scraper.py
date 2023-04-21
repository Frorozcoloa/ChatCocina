from pathlib import Path

from scraper_code.recetas_pais.scrapper import RecetaPais
from scraper_code.recetas_pais.links import Recetas



def get_info():
       RecetaPais().main()

def get_links():
       Recetas().main()

if __name__ == "__main__":
       get_info()
