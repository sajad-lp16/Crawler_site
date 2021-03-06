import os
import re


def splitter(name):
    *_, ext = os.path.splitext(name)
    return ext


def file_name_setter(instance, file_name):
    ext = splitter(file_name)
    return f'movie_pics/{instance.name}{ext}'


def generate_slug(value):
    pattern = r'[\s\.]+'
    slug = re.sub(pattern, '-', value, flags=re.M)
    return slug
