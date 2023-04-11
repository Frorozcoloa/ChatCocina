import numpy as np
from pathlib import Path

from bs4 import BeautifulSoup
import pandas as pd
from newspaper import Article

from scraper_code.logging import logging


DATASET = Path(__file__).parent.parent / "Datasets"
LINKS = DATASET/"Links"
SCRAPPER = DATASET/"Scrapper"
COMPLETED = DATASET/"Completed"
class Scrapper:
    
    def __init__(self, name):
        self.links_path = LINKS / name
        self.scrapper_directory = SCRAPPER / name
        self.completed_directory = COMPLETED / name
        self.scrapper_directory.mkdir(exist_ok=True)
        self.completed_directory.mkdir(exist_ok=True)
    
    def gets_html(self, url):
        article = Article(url, lenguage='es')
        article.download()
        article.parse()
        return article
    
    def main(self):
        links_gen = self.links_path.glob("*.txt")
        for links_batch in links_gen:
            print(f":star: Processing {links_batch}")
            links = np.loadtxt(fname=links_batch, dtype=str).tolist()
            values, errors = self.gets_batch(links)
            # Prepare datasets
            file_save = self.scrapper_directory/links_batch.name.replace(".txt", ".csv")
            #Save dataset
            pd.DataFrame(values).to_csv(file_save, index=False)
            #Saver errors
            with  self.scrapper_directory.with_name("errors.txt").open(mode='a') as f:
                f.write('\n'.join(errors))
            print(f":white_check_mark: Done {links_batch}")
            #Cut to completed
            links_batch.rename(self.completed_directory/links_batch.name)

    def gets_batch(self, links):
        values = []
        errors = []
        for url in links:
            try:
                article = self.gets_html(url)
                title = article.title
                date = article.publish_date
                url = article.url
                text = article.text
                info = {
                    "url": url,
                    "title": title,
                    "date": date,
                    "text": text,
                }
                values.append(info)
                print(f"\t :smiley: {url} done")
            except AttributeError:
                print(f"\t :angry: Error in {url}")
                errors.append(url)
        return values, errors
            
        
    
    
    