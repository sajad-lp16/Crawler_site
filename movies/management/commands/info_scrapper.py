from bs4 import BeautifulSoup
from requests import get
from movies.management.commands import constants


class Crawl:
    def __init__(self):
        self.main_page = self._get_from_target(constants.URL)
        self.data = self.data_mapper()

    @staticmethod
    def _get_from_target(url):
        response = get(url).text
        return BeautifulSoup(response, 'html.parser')

    def crawl_data(self):
        return self.main_page.select_one('.gnres').select('a')

    def crawl_urls(self):
        data = self.crawl_data()
        return [item.get('href') for item in data]

    def crawl_genres(self):
        data = self.crawl_data()
        return [item.text for item in data]

    def data_mapper(self):
        genres = self.crawl_genres()
        urls = self.crawl_urls()
        return list(zip(genres, urls))

