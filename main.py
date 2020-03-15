from MyHtmlParser import MyHtmlParser
from sources import data

if __name__ == '__main__':

    for d in data:

        parsed = MyHtmlParser(dataset_name=d.get("dataset"), url=d.get("url"))
        parsed.set_range_dates(d.get("period"))
        parsed.retrieve_data()

