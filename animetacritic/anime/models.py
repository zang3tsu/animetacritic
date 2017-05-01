from datetime import datetime

from django.db import models


class Anime(models.Model):
    SEASONS = (
        ('Spr', 'Spring'),
        ('Sum', 'Summer'),
        ('Fal', 'Fall'),
        ('Win', 'Winter')
    )
    YEARS = [(y, y) for y in range(1900, datetime.now().year + 6)]

    title = models.CharField(max_length=200, primary_key=True)
    season = models.CharField(max_length=3, choices=SEASONS)
    year = models.PositiveSmallIntegerField(choices=YEARS)
    anidb = models.ForeignKey(
        'AniDB', on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name='AniDB')
    ann = models.ForeignKey(
        'AnimeNewsNetwork', on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name='AnimeNewsNetwork')
    mal = models.ForeignKey(
        'MyAnimeList', on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name='MyAnimeList')
    kitsu = models.ForeignKey(
        'Kitsu', on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name='Kitsu')
    tot_ratings = models.FloatField('total ratings', null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Anime'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class RatingsSiteModel(models.Model):
    aid = models.PositiveIntegerField(primary_key=True, verbose_name='AID')
    url = models.CharField(max_length=100, verbose_name='URL')
    raw_ratings = models.FloatField(null=True, blank=True)
    nor_ratings = models.FloatField(
        'normalized ratings', null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class AniDB(RatingsSiteModel):

    class Meta:
        verbose_name = 'AniDB'
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'AnimeDB: ' + self.aid


class AnimeNewsNetwork(RatingsSiteModel):

    class Meta:
        verbose_name = 'AnimeNewsNetwork'
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'AnimeNewsNetwork: ' + self.aid


class MyAnimeList(RatingsSiteModel):

    class Meta:
        verbose_name = 'MyAnimeList'
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'MyAnimeList: ' + self.aid


class Kitsu(RatingsSiteModel):

    class Meta:
        verbose_name = 'Kitsu'
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'Kitsu: ' + self.aid
