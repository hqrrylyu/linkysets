# Generated by Django 3.0.7 on 2020-07-14 16:25

from django.contrib.postgres.operations import TrigramExtension, UnaccentExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("entries", "0002_auto_20200714_1625"),
    ]

    operations = [
        UnaccentExtension(),
        TrigramExtension(),
    ]