data = {
    "total_load": [
        {
            "url": "https://transparency.entsoe.eu/load-domain/r2/totalLoadR2/show?name=&defaultValue=true&"
                   "viewType=TABLE&areaType=BZN&atch=false&dateTime.dateTime={datetime}|UTC|DAY&"
                   "biddingZone.values=CTY|10YPT-REN------W!BZN|10YPT-REN------W&"
                   "dateTime.timezone=UTC&dateTime.timezone_input=UTC",
            "period": ("2015-1-1", "2020-4-30"),
            "dataset": "Portugal load"
        },
        {
            "url": "https://transparency.entsoe.eu/load-domain/r2/totalLoadR2/show?name=&defaultValue=false&"
                   "viewType=TABLE&areaType=BZN&atch=false&dateTime.dateTime={datetime}|UTC|DAY&"
                   "biddingZone.values=CTY|10YES-REE------0!BZN|10YES-REE------0&dateTime.timezone=UTC&d"
                   "ateTime.timezone_input=UTC",
            "period": ("2015-1-1", "2020-4-30"),
            "dataset": "Spain load"
        },
        {
            "url": "https://transparency.entsoe.eu/load-domain/r2/totalLoadR2/show?name=&defaultValue=false&"
                   "viewType=TABLE&areaType=BZN&atch=false&dateTime.dateTime={datetime}|UTC|DAY&"
                   "biddingZone.values=CTY|10YIE-1001A00010!BZN|10Y1001A1001A59C&dateTime.timezone=UTC&"
                   "dateTime.timezone_input=UTC",
            "period": ("2015-1-1", "2020-4-30"),
            "dataset": "Ireland load"
        },
        {
            "url": "https://transparency.entsoe.eu/load-domain/r2/totalLoadR2/show?name=&defaultValue=false&"
                   "viewType=TABLE&areaType=CTY&atch=false&dateTime.dateTime={datetime}|UTC|DAY&"
                   "biddingZone.values=CTY|10Y1001A1001A83F!CTY|10Y1001A1001A83F&dateTime.timezone=UTC&"
                   "dateTime.timezone_input=UTC",
            "period": ("2015-1-1", "2020-4-30"),
            "dataset": "Germany load"
        },
        {
            "url": "https://transparency.entsoe.eu/load-domain/r2/totalLoadR2/show?name=&defaultValue=false&"
                   "viewType=TABLE&areaType=CTY&atch=false&dateTime.dateTime={datetime}|UTC|DAY&"
                   "biddingZone.values=CTY|10YIE-1001A00010!CTY|10YIE-1001A00010&dateTime.timezone=UTC&"
                   "dateTime.timezone_input=UTC",
            "period": ("2015-1-1", "2020-4-30"),
            "dataset": "Ireland load"
        },
        {
            "url": "https://transparency.entsoe.eu/load-domain/r2/totalLoadR2/show?name=&defaultValue=false&"
                   "viewType=TABLE&areaType=CTY&atch=false&dateTime.dateTime={datetime}|UTC|DAY&"
                   "biddingZone.values=CTY|10YIT-GRTN-----B!CTY|10YIT-GRTN-----B&dateTime.timezone=UTC&"
                   "dateTime.timezone_input=UTC",
            "period": ("2015-1-1", "2020-4-30"),
            "dataset": "Italy load"
        },

    ],
    "production_type": [
        {
            "url": "https://transparency.entsoe.eu/generation/r2/installedGenerationCapacityAggregation/show?"
                   "name=&defaultValue=false&viewType=TABLE&areaType=BZN&atch=false&"
                   "dateTime.dateTime={start}|UTC|YEAR&dateTime.endDateTime={end}|UTC|YEAR&"
                   "area.values=CTY|10YPT-REN------W!BZN|10YPT-REN------W&productionType.values=B01&"
                   "productionType.values=B02&productionType.values=B03&productionType.values=B04&"
                   "productionType.values=B05&productionType.values=B06&productionType.values=B07&"
                   "productionType.values=B08&productionType.values=B09&productionType.values=B10&"
                   "productionType.values=B11&productionType.values=B12&productionType.values=B13&"
                   "productionType.values=B14&productionType.values=B20&productionType.values=B15&"
                   "productionType.values=B16&productionType.values=B17&productionType.values=B18&"
                   "productionType.values=B19",
            "period": ("2015", "2020"),
            "dataset": "Portugal production type",
        },
{
            "url": "https://transparency.entsoe.eu/generation/r2/installedGenerationCapacityAggregation/show?"
                   "name=&defaultValue=false&viewType=TABLE&areaType=CTY&atch=false"
                   "&dateTime.dateTime={start}|UTC|YEAR&dateTime.endDateTime={end}|UTC|YEAR&"
                   "area.values=CTY|10YIT-GRTN-----B!CTY|10YIT-GRTN-----B&productionType.values=B01&"
                   "productionType.values=B02&productionType.values=B03&productionType.values=B04&"
                   "productionType.values=B05&productionType.values=B06&productionType.values=B07&"
                   "productionType.values=B08&productionType.values=B09&productionType.values=B10&"
                   "productionType.values=B11&productionType.values=B12&productionType.values=B13&"
                   "productionType.values=B14&productionType.values=B20&productionType.values=B15&"
                   "productionType.values=B16&productionType.values=B17&productionType.values=B18&"
                   "productionType.values=B19",
            "period": ("2015", "2020"),
            "dataset": "Italy production type"
        },
{
            "url": "https://transparency.entsoe.eu/generation/r2/installedGenerationCapacityAggregation/show?"
                   "name=&defaultValue=false&viewType=TABLE&areaType=CTY&atch=false&"
                   "dateTime.dateTime={start}|UTC|YEAR&dateTime.endDateTime={end}|UTC|YEAR&"
                   "area.values=CTY|10YIE-1001A00010!CTY|10YIE-1001A00010&productionType.values=B01&"
                   "productionType.values=B02&productionType.values=B03&productionType.values=B04&"
                   "productionType.values=B05&productionType.values=B06&productionType.values=B07&"
                   "productionType.values=B08&productionType.values=B09&productionType.values=B10&"
                   "productionType.values=B11&productionType.values=B12&productionType.values=B13&"
                   "productionType.values=B14&productionType.values=B20&productionType.values=B15&"
                   "productionType.values=B16&productionType.values=B17&"
                   "productionType.values=B18&productionType.values=B19",
            "period": ("2015", "2020"),
            "dataset": "Ireland production type"
        },
{
            "url": "https://transparency.entsoe.eu/generation/r2/installedGenerationCapacityAggregation/show?"
                   "name=&defaultValue=false&viewType=TABLE&areaType=CTY&atch=false&"
                   "dateTime.dateTime={start}|UTC|YEAR&dateTime.endDateTime={end}|UTC|YEAR&"
                   "area.values=CTY|10Y1001A1001A83F!CTY|10Y1001A1001A83F&"
                   "productionType.values=B01&productionType.values=B02&productionType.values=B03&"
                   "productionType.values=B04&productionType.values=B05&productionType.values=B06&"
                   "productionType.values=B07&productionType.values=B08&productionType.values=B09&"
                   "productionType.values=B10&productionType.values=B11&productionType.values=B12&"
                   "productionType.values=B13&productionType.values=B14&productionType.values=B20&"
                   "productionType.values=B15&productionType.values=B16&productionType.values=B17&"
                   "productionType.values=B18&productionType.values=B19",
            "period": ("2015", "2020"),
            "dataset": "Germany production type"
        },
        {
            "url": "https://transparency.entsoe.eu/generation/r2/installedGenerationCapacityAggregation/show?"
                   "name=&defaultValue=true&viewType=TABLE&areaType=BZN&atch=false&"
                   "dateTime.dateTime={start}|UTC|YEAR&dateTime.endDateTime={end}|UTC|YEAR"
                   "&area.values=CTY|10YES-REE------0!BZN|10YES-REE------0&productionType.values=B01&"
                   "productionType.values=B02&productionType.values=B03&productionType.values=B04&"
                   "productionType.values=B05&productionType.values=B06&productionType.values=B07&"
                   "productionType.values=B08&productionType.values=B09&productionType.values=B10&"
                   "productionType.values=B11&productionType.values=B12&productionType.values=B13&"
                   "productionType.values=B14&productionType.values=B20&productionType.values=B15&"
                   "productionType.values=B16&productionType.values=B17&productionType.values=B18&"
                   "productionType.values=B19",
            "period": ("2015", "2020"),
            "dataset": "Spain production type"
        }
    ],
}
