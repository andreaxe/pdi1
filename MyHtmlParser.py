import os
import time
import pandas as pd
from models.MyModel import ProductionType, TotalLoad

from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime, timedelta


class MyHtmlParser:

    RANGE_YEAR = 'range_year'
    RANGE_DAYS = 'range_days'

    """This class purpose is to parse an HTML page"""

    def __init__(self, url, dataset_name, dataset_type, columns=None):
        """
        :param url: the url required to parse an html table
        :param columns:
        """
        self.url = url
        self.data = None
        self.days = None
        self.range_year = None
        self.columns = columns
        self.dataset_name = dataset_name
        self.dataset_type = dataset_type

    def set_url(self, url):
        """
        Change the url to be parsed
        :param url:
        :return:
        """

        self.url = url

    def set_range_dates(self, period):
        """
        first is required to verify what type of data is being retrieved using the date value as a known
        required dataset
        :param period: a tuple containing strings with start and end dates
        :return:
        """

        fmts = {'%Y': self.RANGE_YEAR, '%Y-%m-%d': self.RANGE_DAYS}

        for fmt, value in fmts.items():
            try:
                start = datetime.strptime(period[0], fmt)
                end = datetime.strptime(period[1], fmt)

                if value == self.RANGE_DAYS:
                    date_array = (start + timedelta(days=x) for x in range(0, (end - start).days))
                    self.days = list(date_array)
                elif value == self.RANGE_YEAR:
                    self.range_year = (start, end)
                break

            except ValueError:
                pass

    def retrieve_data(self):

        # is going to retrieve data looping through days and store the result into a CSV File
        if self.days is not None:

            total_load = TotalLoad()
            for day in self.days:
                time.sleep(1)
                # "urllib.error.HTTPError: HTTP Error 429: Too Many Requests"
                day = day.strftime("%d.%m.%Y+00:00")
                url = self.url.format(datetime=day)
                print("Parsing day: {}".format(day))
                res = self.parse_data(url)
                self.data = pd.DataFrame(data=res)
                self.save(day)
                total_load.save(df=self.data, day=day, country=self.dataset_name)

        if self.range_year is not None:

            production_type = ProductionType()
            url = self.url.format(start=self.range_year[0].strftime("%d.%m.%Y+00:00"),
                                  end=self.range_year[1].strftime("%d.%m.%Y+00:00"))
            res = self.parse_data(url)
            self.data = pd.DataFrame(data=res)
            self.save(self.dataset_name)
            production_type.save(df=self.data, range_dates=self.range_year, country=self.dataset_name)

            pass

    @staticmethod
    def parse_data(url):

        #  to avoid "urllib.error.HTTPError: HTTP Error 429: Too Many Requests"
        time.sleep(1)

        page = urlopen(url)
        soup = BeautifulSoup(page.read())
        table = soup.find('tbody')
        res, row = [], []

        for tr in table.find_all_next('tr'):
            for td in tr.find_all('td'):
                row.append(td.text.strip())
            res.append(row)
            row = []

        return res

    def save(self, day):

        # create the csv files
        os.makedirs(os.path.join('files', self.dataset_name), exist_ok=True)
        self.data.to_csv(os.path.join('files', self.dataset_name, day + '.csv'), header=None, index=False)
        if self.dataset_type == 'total_load':
            pass


