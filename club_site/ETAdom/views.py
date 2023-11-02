from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context= {"name":1}
    return render(request, 'ETAdom/calendar.html', context)
# Create your views here.
