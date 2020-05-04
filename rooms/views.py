
from django.views.generic import ListView, DetailView
from django.http import Http404

# from django.urls import reverse
from django.utils import timezone
from django.shortcuts import render  # ,redirect
from django_countries import countries
from . import models


# Create your views here.


class HomeView(ListView):
    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


class RoomDetail(DetailView):
    """RoomDetail Definition"""

    model = models.Room


""" def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        raise Http404 #return render(request, "404.html")이렇게 안해도 debug 모드 false로 하고 template 안에 404.html파일 만들어 놓으면 자동으로 rendering됨...
       # return redirect(reverse("core:home"))
        #return redirect("")
 """


def serch(request):
    print(vars(request))
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country=request.GET.get("country","KR")
    room_type = int(request.GET.get("room_type",0))
    room_types = models.RoomType.objects.all()
    form={  
        "city" : city,
        "s_room_type":room_type,
        "s_country":country
    }
    choices={"countries" : countries,"room_types" : room_types,

    }
    return render(request, "rooms/search.html", {**form,**choices})
