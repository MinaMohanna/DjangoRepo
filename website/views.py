from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index_view(request):
    return HttpResponse (" <h1> This is my HOME </h1>")


def contact_view(request):
    return HttpResponse (" <h1> This is my Contact </h1>")

def about_view(request):
    return HttpResponse (" <h1> This is my About </h1>")
    