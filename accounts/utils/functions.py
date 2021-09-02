import os


def base_name(file_name):
    name, ext = os.path.splitext(file_name)
    return ext


def rename_file(instance, file_name):
    ext = base_name(file_name)
    return f'profiles/{instance}/{instance}{ext}'
