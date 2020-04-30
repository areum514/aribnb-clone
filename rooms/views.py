from math import ceil
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models


# Create your views here.


def all_rooms(request):

    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.get_page(int(page))
        return render(request, "rooms/home.html", {"page": rooms})
    except EmptyPage:
        rooms = paginator.page(1)
        return redirect("/")


# 모든 exception에 대응하고싶다면 그냥except: 하면됨~
