
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
    country =request.GET.get("country","KR")
    room_type = int(request.GET.get("room_type",0))
    price =int(request.GET.get("price",0))
    guests =int(request.GET.get("guests",0))
    bedromms =int(request.GET.get("bedromms",0))
    beds =int(request.GET.get("beds",0))
    baths =int(request.GET.get("baths",0))
    super_host=request.GET.get("super_host",False)
    instant = request.GET.get("instant", False)
    s_amenities = request.GET.getlist("amenities")
    s_facilities = request.GET.getlist("facilities")
 
    form={  
        "city" : city,
        "s_room_type":room_type,
        "s_country":country,
        "price": price,
        "guests": guests,
        "bedromms": bedromms,
        "beds": beds,
        "baths":baths,
        "s_amenities":s_amenities,
        "s_facilities":s_facilities,
        "instant":instant,
        "super_host":super_host,
    }

    room_types = models.RoomType.objects.all()
    amenities=models.Amenity.objects.all()
    facilities=models.Facility.objects.all()

    choices={
        "countries" : countries,
        "room_types" : room_types,
        "amenities":amenities,
        "facilities":facilities,
    }
    return render(request, "rooms/search.html", {**form,**choices})
