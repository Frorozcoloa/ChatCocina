from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
from wordcloud import WordCloud
from spacy.lang.es.stop_words import STOP_WORDS

@pd.api.extensions.register_dataframe_accessor("utils_text")
class TextAccessor:
    def __init__(self, pandas_obj):
        self._obj = pandas_obj
    
    def _filter_column_text(self):
        return self._obj.select_dtypes(include=['object']).columns
    
    def plot_word_cloud(self, max_words=100, max_font_size=50, width=800, height=400):
        filter_columns = self._filter_column_text()
        num_columns = len(filter_columns)
        fig, axs =plt.subplots(num_columns,figsize=(20, 20))
        for column, ax in zip(filter_columns, axs):
            world_cloud = WordCloud(max_words=max_words, 
                  max_font_size=max_font_size, 
                  width=width, height=height, 
                  background_color="white", 
                  stopwords=STOP_WORDS
                  ).generate(self._obj[column].str.cat())
            ax.imshow(world_cloud, interpolation="bilinear")
            ax.axis("off")
            ax.set_title(column)
        plt.show()
    
    def plot_length_text(self):
        filter_columns = self._filter_column_text()
        num_columns = len(filter_columns)
        fig, axs =plt.subplots(num_columns,figsize=(20, 20))
        for column, ax in zip(filter_columns, axs):
            self._obj[column].str.len().plot.hist(ax=ax)
            ax.set_title(column)
        plt.show()
    
    def plot_boxplot(self):
        filter_columns = self._filter_column_text()
        num_columns = len(filter_columns)
        fig, axs =plt.subplots(num_columns,figsize=(20, 20))
        for column, ax in zip(filter_columns, axs):
            self._obj[column].str.len().plot.box(ax=ax)
            ax.set_title(column)
        plt.show()