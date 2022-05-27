"""
All tool to scrap
"""
from scrapy.crawler import CrawlerProcess
from generate_csv import PicWebSite


class ScrappingPicture:
    """
    Scrapping picture from web site
    """

    def __init__(self):
        # run spider
        process = CrawlerProcess(settings={
            'FEED_URI': 'name_company_link_company_size.csv',
            'FEED_FORMAT': 'csv'
        })
        process.crawl(PicWebSite)
        process.start()

    # TODO Scrapping web site 1 time per week to be able to get tendance of best selling pictures
    # TODO get all pic for compliance pic
    # Validate compliance and/or tendance of picture posted
    # TODO Host .py and run it 1 time/da