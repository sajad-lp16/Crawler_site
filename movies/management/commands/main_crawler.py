import re

from django.core.management.base import BaseCommand

from movies.utils import info_scrapper
from movies.utils import functions
from concurrent.futures import ThreadPoolExecutor
from movies import models


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.crawler = info_scrapper.CrawlModels()

    def build_models(self, genre_data):
        slug = functions.generate_slug(genre_data[0])
        genre = models.Genre.objects.create(title=genre_data[0], slug=slug)
        posts = self.crawler.crawl_genres_page(genre_data[1])
        with ThreadPoolExecutor(max_workers=4) as exe:
            movies = exe.map(self.crawler.crawl_movies, posts)

        for movie in movies:
            models.Movie.objects.create(
                genre=genre,
                **movie
            )

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('building genres'))
        data = self.crawler.data_mapper()
        with ThreadPoolExecutor(max_workers=4) as execute:
            execute.map(self.build_models, data)
