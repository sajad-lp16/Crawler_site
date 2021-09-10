# Generated by Django 3.2.6 on 2021-09-09 19:34

import accounts.utils.functions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='unknown.png', upload_to=accounts.utils.functions.rename_file, verbose_name='avatar'),
        ),
    ]