from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import *


@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    # vazifa uchun o'zgartirish
    list_display = ["id", "ism", "jins", "tugulgan_kun", "tirik", "kitoblar_soni"]
    list_display_links = ["id", "ism"]  # links --> id , ism
    list_editable = ["tirik", "kitoblar_soni"]  # editable --> kitoblar soni va tirikligi
    search_fields = ["ism"]
    search_help_text = "Ism ustunlari bo'yicha qidiring"
    list_filter = ["tirik"]  # filter --> tirik
    ordering = ["id"]
    date_hierarchy = "tugulgan_kun"
    list_per_page = 10


@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    list_display = ["id", "nom", "sahifa", "janr", "muallif"]
    list_display_links = ["id", "nom"]
    search_fields = ["id", "nom", "muallif__ism"]
    search_help_text = "Id , nom va muallif ustunlari bo'yicha qidiring"
    list_filter = ["janr", "muallif"]
    list_editable = ["sahifa"]
    autocomplete_fields = ["muallif"]


@admin.register(Kutubxonachi)
class KutubxonachiAdmin(admin.ModelAdmin):
    list_display = ["id", "ism", "ish_vaqti"]
    list_display_links = ["id", "ism"]
    search_fields = ["ism"]
    search_help_text = "Ism ustunlari bo'yicha qidiring"
    list_filter = ["ish_vaqti"]


admin.site.register(Talaba)
# admin.site.register(Muallif)
# admin.site.register(Kitob)
# admin.site.register(Kutubxonachi)
admin.site.register(Record)

# admin.site.unregister(Group)
# admin.site.unregister(User)
