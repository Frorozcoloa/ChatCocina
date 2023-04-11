from pathlib import Path

from scraper_code.Peque.scraper import ScrapperPeque


def main():
    scrapper = ScrapperPeque("Peque")
    scrapper.main()

if __name__ == "__main__":
    main()

