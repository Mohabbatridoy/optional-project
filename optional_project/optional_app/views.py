from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1> project runed</h1> <hr> <a href='contact/'>ContactPage</a> <a href='about/'>aboutPage</a>")
def contact(request):
    return HttpResponse("this is contact page..... <a href='/'>HomePage</a> <a href='/about/'>AboutPage</a>")
def about(request): 
    return HttpResponse("this is about us page <a href='/'>HomePage</a> <a href='/contact/'>ContactPage</a>")