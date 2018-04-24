from django.shortcuts import render


def index(request):
    return render(request, "mainapp/index.html")


def alarms(request):
    return render(request, "mainapp/alarms.html")


def positions(request):
    return render(request, "mainapp/positions.html")


def params(request):
    return render(request, "mainapp/params.html")


def cctv(request):
    return render(request, "mainapp/cctv.html")


def changeable_settings(request):
    return render(request, "mainapp/changeable_settings.html")


def curr_params(request):
    return render(request, "mainapp/curr_params.html")
