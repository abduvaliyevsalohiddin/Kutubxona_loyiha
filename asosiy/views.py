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
    if request.method == 'POST':
        ism = request.POST.get("ism")
        kurs = request.POST.get("kurs")
        kitob_soni = request.POST.get("kitob_soni")
        Talaba(ism=ism, kurs=kurs, kitob_soni=kitob_soni).save()
        return redirect("/hamma_talabalar/")
    soz = request.GET.get("qidirish_sozi")
    natija = Talaba.objects.all()
    if soz:
        natija = natija.filter(ism__contains=soz)
    content = {
        "talabalar": natija
    }
    return render(request, "mashq/hamma_talabalar.html", content)


def talaba_ochir(request, son):
    Talaba.objects.get(id=son).delete()
    return redirect("/hamma_talabalar/")


def hamma_muallif(request):
    if request.method == 'POST':
        Muallif.objects.create(
            ism=request.POST.get("ism"),
            jins=request.POST.get("jins"),
            tugulgan_kun=request.POST.get("tugulgan_kun"),
            kitoblar_soni=request.POST.get("kitoblar_soni"),
            tirik=request.POST.get("tirik") == "on",
        )

    soz = request.GET.get("qidirish_sozi")
    natija = Muallif.objects.all()
    if soz:
        natija = natija.filter(ism__contains=soz)
    content = {
        "mualliflar": natija
    }
    return render(request, "mashq/hamma_muallif.html", content)


def muallif_ochir(request, son):
    Muallif.objects.get(id=son).delete()
    return redirect("/hamma_mualliflar/")


def hamma_kitob(request):
    if request.method == 'POST':
        Kitob.objects.create(
            nom=request.POST.get("nom"),
            janr=request.POST.get("janr"),
            sahifa=request.POST.get("sahifa"),
            muallif=Muallif.objects.get(id=request.POST.get("muallif")),
        )
    soz = request.GET.get("qidirish_sozi")
    natija = Kitob.objects.all()
    if soz:
        natija = natija.filter(muallif__ism__contains=soz) | natija.filter(nom__contains=soz)

    content = {
        "kitoblar": natija,
        "mualliflar": Muallif.objects.all()
    }
    return render(request, "mashq/hamma_kitoblar.html", content)


def hamma_record(request):
    if request.method == 'POST':
        Record.objects.create(
            talaba=Talaba.objects.get(id=request.POST.get("talaba")),
            kitob=Kitob.objects.get(id=request.POST.get("kitob")),
            kutubxonachi=Kutubxonachi.objects.get(id=request.POST.get("kutubxonachi"))
        )
    soz = request.GET.get("qidirish_sozi")
    natija = Record.objects.all()
    if soz:
        natija = natija.filter(talaba__ism__contains=soz)

    content = {
        "record": natija,
        "talabalar": Talaba.objects.all(),
        "kitoblar": Kitob.objects.all(),
        "kutubxonachilar": Kutubxonachi.objects.all()
    }
    return render(request, "mashq/hamma_record.html", content)


def record_ochir(request, son):
    Record.objects.get(id=son).delete()
    return redirect("/hamma_recordlar/")


# mashq -- 15-10-2023

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


def hamma_kutubxonachilar(request):
    if request.method == 'POST':
        Kutubxonachi.objects.create(
            ism=request.POST.get("ism"),
            ish_vaqti=request.POST.get("ish_vaqti"),
        )

    soz = request.GET.get("qidirish_sozi")
    natija = Kutubxonachi.objects.all()
    if soz:
        natija = natija.filter(ism__contains=soz)

    soat = []
    for i in range(25):
        soat.append(i)

    content = {
        "kutubxonachilar": natija,
        "soat": soat
    }
    return render(request, "mashq/hamma_kutubxonachilar.html", content)


def kutubxonachi_ochir(request, son):
    Kutubxonachi.objects.get(id=son).delete()
    return redirect("/hamma_kutubxonachilar/")


def talaba_update(request, son):
    if request.method == 'POST':
        Talaba.objects.filter(id=son).update(
            kurs=request.POST.get("kurs"),
            kitob_soni=request.POST.get("kitob_soni")
        )
        return redirect('/hamma_talabalar/')

    content = {
        "talaba": Talaba.objects.get(id=son)
    }
    return render(request, 'mashq/talaba_update.html', content)
