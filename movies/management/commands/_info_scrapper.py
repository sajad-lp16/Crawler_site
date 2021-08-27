import re
from bs4 import BeautifulSoup
from requests import get
from movies.management.commands import _constants
from django.core.files.uploadedfile import SimpleUploadedFile
import uuid


class Singleton(type):
    __objects = {}

    def __call__(cls, *args, **kwargs):
        obj = Singleton.__objects
        if obj.get(cls.__name__) is None:
            obj[cls.__name__] = super().__call__(*args, **kwargs)
        return obj[cls.__name__]


class BaseCrawl(metaclass=Singleton):
    def __init__(self):
        self.main_page = self.get_from_target(_constants.URL)

    @staticmethod
    def get_from_target(url):
        response = get(url).text
        return BeautifulSoup(response, 'html.parser')

    def _crawl_data(self):
        return self.main_page.select_one('.gnres').select('a')

    def crawl_urls(self):
        data = self._crawl_data()
        return [item.get('href') for item in data]

    def crawl_genres(self):
        data = self._crawl_data()
        return [item.text for item in data]

    def data_mapper(self):
        return list(zip(self.crawl_genres(), self.crawl_urls()))


class CrawlModels(BaseCrawl):
    def __init__(self):
        super().__init__()
        self.data = self.data_mapper()

    def crawl_genres_page(self, url):
        res = self.get_from_target(url)
        return res.select('article.post')[1:]

    @staticmethod
    def crawl_movies(movie):
        result = {}
        pattern = r'[^:]*'
        data = movie.select_one('div.contents').find_all(
            'p', {'style': 'text-align: right;'}
        )
        name = movie.select_one('h2').text.replace('دانلود فیلم ', '')
        result['name'] = name
        clean_data = [item.text for item in data]
        for item in clean_data:
            try:
                data_type = re.search(pattern, item).group()
                result[_constants.TRANSLATOR[data_type]] = item.replace(
                    data_type, ''
                ).replace(':', '').strip()
            except:
                pass
        try:
            image_url = movie.select_one('div.contents').select_one('img').get('src')
            file_path = f'movies/management/commands/images/{int(uuid.uuid4())}' + '.jpg'
            with open(file_path, 'wb') as file:
                file.write(get(image_url).content)
            file = open(file_path, 'rb')
            result['cover'] = SimpleUploadedFile(file.name, file.read())
            file.close()
        except:
            pass
        return result
