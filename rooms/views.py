from datetime import datetime
from django.shortcuts import render


# Create your views here.


def all_rooms(request):
    # return HttpResponse(content="hello")
    now = datetime.now()
    hungry = False
    return render(request, "all_rooms.html", context={"now": now, "hungry": hungry})
