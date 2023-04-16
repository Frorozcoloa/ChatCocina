import pandas as pd
from wordcloud import WordCloud
from spacy.lang.es.stop_words import STOP_WORDS

class Utils:
    
    @staticmethod
    def get_wordcloud(text, max_words=100, max_font_size=50, width=800, height=400):
        wordcloud = WordCloud(max_words=max_words, max_font_size=max_font_size, width=width, height=height, background_color="white", stopwords=STOP_WORDS)
        wordcloud.generate(text)
        return wordcloud.to_image()
    
