from pathlib import Path

Dataset = Path(__file__).parent.parent.parent / 'Dataset'/  'links.csv'

class Download:
    def __init__(self, scrapper)