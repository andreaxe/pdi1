from MyHtmlParser import MyHtmlParser

if __name__ == '__main__':

    data = [
        {
            "url": "https://transparency.entsoe.eu/load-domain/r2/totalLoadR2/show?name=&defaultValue=true&"
                   "viewType=TABLE&areaType=BZN&atch=false&dateTime.dateTime={datetime}|UTC|DAY&"
                   "biddingZone.values=CTY|10YPT-REN------W!BZN|10YPT-REN------W&"
                   "dateTime.timezone=UTC&dateTime.timezone_input=UTC",
            "period": ("2013-2-1", "2020-3-12"),
            "dataset": "Portugal load"
        },
        {
            "url": "https://transparency.entsoe.eu/load-domain/r2/totalLoadR2/show?name=&defaultValue=false&"
                   "viewType=TABLE&areaType=BZN&atch=false&dateTime.dateTime={datetime}|UTC|DAY&"
                   "biddingZone.values=CTY|10YES-REE------0!BZN|10YES-REE------0&dateTime.timezone=UTC&d"
                   "ateTime.timezone_input=UTC",
            "period": ("2013-2-1", "2020-3-12"),
            "dataset": "Spain load"
        }
    ]

    for d in data:

        parsed = MyHtmlParser(dataset_name=d.get("dataset"), url=d.get("url"))
        parsed.set_range_dates(d.get("period")[0], d.get("period")[1])
        parsed.retrieve_data()

