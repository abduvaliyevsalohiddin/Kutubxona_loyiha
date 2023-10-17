from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


def salomlash(request):
    return HttpResponse("<h1>Salom , Dunyo!</h1>")


def homepage(request):
    return render(request, "home.html")


def hamma_kitoblar(request):
    content = {
        "kitoblar": Kitob.objects.all()
    }
    return render(request, "kitoblar.html", content)


def ayol_mualliflar_kitoblari(request):
    content = {
        "kitoblar": Kitob.objects.filter(muallif__jins='Ayol')
    }
    return render(request, "mashq/ayollar_kitoblari.html", content)


def kitob(request, son):
    content = {
        "book": Kitob.objects.get(id=son)
    }
    return render(request, "mashq/kitob.html", content)


def hamma_talabalar(request):
    soz = request.GET.get("qidirish_sozi")
    natija = Talaba.objects.all()
    if soz:
        natija = natija.filter(ism__contains=soz)
    content = {
        "talabalar": natija
    }
    return render(request, "mashq/hamma_talabalar.html", content)


def hamma_muallif(request):
    content = {
        "muallif": Muallif.objects.all()
    }
    return render(request, "vazifa/hamma_muallif.html", content)


def hamma_kitob(request):
    soz = request.GET.get("qidirish_sozi")
    natija = Kitob.objects.all()
    if soz:
        natija = natija.filter(muallif__ism__contains=soz) | natija.filter(nom__contains=soz)

    content = {
        "kitoblar": natija
    }
    return render(request, "vazifa/hamma_kitoblar.html", content)


def hamma_record(request):
    content = {
        "record": Record.objects.all()
    }
    return render(request, "vazifa/hamma_record.html", content)


# mashq -- 15-10-2023

def talaba_ochir(request, son):
    Talaba.objects.get(id=son).delete()
    return redirect("/hamma_talabalar/")


def kitob_ochir(request, son):
    Kitob.objects.get(id=son).delete()
    return redirect("/hamma_kitoblar/")


def tanlangan_muallif(request, ismi):
    content = {
        "x": Muallif.objects.get(ism=ismi)
    }
    return render(request, "vazifa/tanlangan_muallif.html", content)


def kitob(request, son):
    content = {
        "book": Kitob.objects.get(id=son)
    }
    return render(request, "vazifa/kitob.html", content)


def tirik_muallif(request):
    content = {
        "mualliflar": Muallif.objects.filter(tirik=True)
    }
    return render(request, "vazifa/tirik_muallif.html", content)


def sahifa_kop_kitob(request):
    content = {
        "kitoblar": Kitob.objects.order_by("-sahifa")[:3]
    }
    return render(request, "vazifa/sahifa_kop_kitob.html", content)


def kitobi_kop_muallif(request):
    content = {
        "mualliflar": Muallif.objects.order_by("-kitoblar_soni")[:3]
    }
    return render(request, "vazifa/kitobi_kop_muallif.html", content)


def record_tartiblash(request):
    content = {
        "recordlar": Record.objects.order_by("-olingan_sana")[:3]
    }
    return render(request, "vazifa/record_tartiblash.html", content)


def tirik_muallif_kitob(request):
    content = {
        "kitoblar": Kitob.objects.filter(muallif__tirik=True)
    }
    return render(request, "vazifa/tirik_muallif_kitob.html", content)

def badiiy_kitoblar(request):
    content = {
        "kitoblar": Kitob.objects.filter(janr="Badiiy")
    }
    return render(request, "vazifa/badiiy_kitoblar.html", content)


def eng_yoshi_katta_muallif(request):
    content = {
        "mualliflar": Muallif.objects.order_by("tugulgan_kun")[:3]
    }
    return render(request, "vazifa/eng_yoshi_katta_muallif.html", content)


def kitob_muallif(request):
    content = {
        "kitoblar": Kitob.objects.filter(muallif__kitoblar_soni__lt=10)
    }
    return render(request, "vazifa/kitob_muallif.html", content)


def tanlangan_record(request, son):
    content = {
        "record": Record.objects.get(id=son)
    }
    return render(request, "vazifa/tanlangan_record.html", content)


def bitiruvchi_talaba_record(request):
    content = {
        "record": Record.objects.filter(talaba__kurs=4)
    }
    return render(request, "vazifa/bitiruvchi_talaba_record.html", content)