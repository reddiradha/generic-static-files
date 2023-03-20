from django.shortcuts import render

# Create your views here.
def team(request):
    return render(request,'team.html')


def virat(request):
    return render(request,'virat.html')


def dhoni(request):
    return render(request,'dhoni.html')


def rohith(request):
    return render(request,'rohith.html')


def sachin(request):
    return render(request,'sachin.html')