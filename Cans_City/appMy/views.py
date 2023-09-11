from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def detail(request, id):
    game = Game.objects.get(id=id)
    deluxe = Game.objects.get(title=game.title, edition=2)
    ultimate = Game.objects.get(title=game.title, edition=3)

    context = {
        'game': game,
        'deluxe': deluxe,
        'ultimate': ultimate
    }

    return render(request, 'detail.html', context)


def pc(request):
    pc = Game.objects.filter(platform=1, edition=1)
    order_by = request.GET.get("order_by")
    query = request.GET.get("searchInput")

    if query:
        pc = pc.filter(Q(title__icontains=query)).distinct

    if order_by == "low":
        pc = pc.order_by('price')

    if order_by == "high":
        pc = pc.order_by('-price')

    context = {
        'pc': pc,
    }

    return render(request, 'pc.html', context)


def ps5(request):
    ps5 = Game.objects.filter(platform=2, edition=1)
    query = request.GET.get("searchInput")

    if query:
        ps5 = ps5.filter(Q(title__icontains=query)).distinct

    context = {
        'ps5': ps5,
    }

    return render(request, 'ps5.html', context)


def xbox(request):
    xbox = Game.objects.filter(platform=3, edition=1)
    query = request.GET.get("searchInput")

    if query:
        xbox = xbox.filter(Q(title__icontains=query)).distinct

    context = {
        'xbox': xbox,
    }

    return render(request, 'xbox.html', context)
