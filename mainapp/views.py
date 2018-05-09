from django.shortcuts import render


def index(request):
    icon_size = 9
    row1 = [
        ['/alarms', 'mainapp/img/sample.png', 'fas fa-exclamation-triangle fa-%sx fa-fw' % icon_size, 'tomato'],
        ['/positions', 'mainapp/img/sample.png', 'fas fa-map-marker-alt fa-%sx fa-fw' % icon_size, 'SpringGreen'],
        ['/params', 'mainapp/img/sample.png', 'fas fa-chart-line fa-%sx fa-fw' % icon_size, 'BlueViolet'],
    ]

    row2 =[
        ['/cctv', 'mainapp/img/sample.png', 'fas fa-video fa-%sx fa-fw' % icon_size, 'DarkTurquoise '],
        ['/changeable_settings', 'mainapp/img/sample.png', 'fas fa-toggle-on fa-%sx fa-fw' % icon_size, 'SlateGray'],
        ['/curr_settings', 'mainapp/img/sample.png', 'fas fa-clipboard-list fa-%sx fa-fw' % icon_size, '#ed8f6d']
    ]
    return render(request, "mainapp/index.html", {"row1": row1, "row2": row2, "whole": row1 + row2})


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


def curr_settings(request):
    return render(request, "mainapp/curr_settings.html")
