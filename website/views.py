from django.shortcuts import render

# Create your views here.
def home(request):
    return(render(request, "website/home.html"))
def portfolios(request):
    return(render(request, "website/portfolios.html"))
def about(request):
    return(render(request, "website/about.html"))
def investments(request):
    return(render(request, "website/investment.html"))
def research(request):
    return(render(request, "website/research.html"))