import os
import pandas as pd

from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime, timedelta


class MyHtmlParser:

    """This class purpose is to parse an HTML page"""

    def __init__(self, url, dataset_name, columns=None):
        """
        :param url: the url required to parse an html table
        :param columns:
        """
        self.url = url
        self.data = None
        self.days = None
        self.columns = columns
        self.dataset_name = dataset_name

    def set_url(self, url):
        """
        Change the url to be parsed
        :param url:
        :return:
        """

        self.url = url

    def set_range_dates(self, period):
        """
        :param period: a tuple containing strings with start and end dates
        :return:
        """
        start = datetime.strptime(period[0], "%Y-%m-%d")
        end = datetime.strptime(period[1], "%Y-%m-%d")
        date_array = (start + timedelta(days=x) for x in range(0, (end - start).days))
        self.days = list(date_array)

    def retrieve_data(self):

        import time
        for day in self.days:

            time.sleep(1)
            day = day.strftime("%d.%m.%Y+00:00")
            url = self.url.format(datetime=day)
            print("Parsing day: {}".format(day))

            page = urlopen(url)
            soup = BeautifulSoup(page.read())
            table = soup.find('tbody')
            res, row = [], []

            for tr in table.find_all_next('tr'):
                for td in tr.find_all('td'):
                    row.append(td.text.strip())
                res.append(row)
                row = []

            self.data = pd.DataFrame(data=res)
            self.save(day)

    def save(self, day):

        os.makedirs(os.path.join('files', self.dataset_name), exist_ok=True)
        self.data.to_csv(os.path.join('files', self.dataset_name, day + '.csv'), header=None, index=False)
