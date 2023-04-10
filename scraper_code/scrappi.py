from newspaper import Article, network
from bs4 import BeautifulSoup
from pathlib import Path

from URL import URLS

PATH_DATASET = Path('Datasets')


def get_links(url):
    article = Article(url)
    article.download()
    article.parse()
    soup = BeautifulSoup(article.html, 'html.parser')
    links = soup.find_all('a', class_='titulo titulo--resultado')
    links = [link.get('href') for link in links]
    return links

def main():
     for info_dict in URLS:
        url_format = info_dict['url']
        tag = info_dict['tag']
        last_page = info_dict['last_page']
        directory = PATH_DATASET/tag.replace(" ", "_")
        directory.mkdir(parents=True, exist_ok=True)
        print(f'Creating directory {directory} for {tag}')
        for page in range(1, last_page + 1):
            filename = directory/f'{page}.txt'
            url = url_format.format(page, tag)
            links = get_links(url)
            filename.write_text('\n'.join(links))
            print(f'\tPage {page} of {last_page} done! for {url}')

if __name__ == '__main__':
   main()