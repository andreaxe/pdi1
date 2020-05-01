from MyHtmlParser import MyHtmlParser
from sources import data

if __name__ == '__main__':

    exclude = []
    for k in data:
        if k in exclude:
            continue
        for v in data[k]:
            parsed = MyHtmlParser(dataset_name=v.get("dataset"), url=v.get("url"), dataset_type=k)
            print(v.get('dataset'))
            parsed.set_range_dates(v.get("period"))
            parsed.retrieve_data()
