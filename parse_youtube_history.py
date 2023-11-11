""" Parser to extract information from Youtube data

Example usage:
    ```python
    import parse_scap as ps
    pa = ps.Parser('assets/data/watch-history.html')
    extract = pa.extract_youtube()
    pa.export_csv(extract)
    ```
"""
import pandas as pd
from bs4 import BeautifulSoup

class Parser:
    """ Parser to extract information from Youtube data """
    def __init__(self, path):
        self.path = path
        self.data = self.get_data_from_file(path)

    def get_data_from_file(self, path) -> str:
        """ Get data from file """
        with open(path, 'r') as f:
            data = f.read()
        return data

    def extract_youtube(self, class_name='content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1') -> pd.DataFrame:
        """ Extracts information from Youtube data """
        soup = BeautifulSoup(self.data, 'html.parser')
        videos = soup.findAll('div', class_=class_name)
        watched = {'title': [], 'channel_name': [], 'video_url': [], 'channel_url': []}
        for video in videos:
            try:
                watched['title'].append(video.find('a').text)
                watched['video_url'].append(video.find('a')['href'])
                a_tags = video.findAll('a')
                if len(a_tags) > 1:
                    channel = a_tags[1]
                    watched['channel_name'].append(channel.text)
                    watched['channel_url'].append(channel['href'])
                else:
                    watched['channel_name'].append(None)
                    watched['channel_url'].append(None)
            except:
                pass
        df_watched = pd.DataFrame(watched)

        # No real title extracted (https instead)
        # + video at link is not available anymore
        # => drop it
        ma = df_watched['title'].str.contains('https') == True
        df_watched = df_watched[~ma]
        return df_watched

    def export_csv(self, df:pd.DataFrame, path:str=None):
        """ Export extracted data to csv """
        suffix = '_extract.csv'
        if not path:
            df.to_csv(self.path + suffix, index=False)
        else:
            df.to_csv(self.path + suffix, index=False)
