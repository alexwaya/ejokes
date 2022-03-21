from django.shortcuts import render
import pyjokes

#import jokes

def index(request):
    jokes = pyjokes.get_joke()
    return render(request, 'index.html', {'jokes:jokes'})