from django.contrib import admin

from .models import Anime, AniDB, AnimeNewsNetwork, MyAnimeList, Kitsu

admin.site.register(Anime)
admin.site.register(AniDB)
admin.site.register(AnimeNewsNetwork)
admin.site.register(MyAnimeList)
admin.site.register(Kitsu)
