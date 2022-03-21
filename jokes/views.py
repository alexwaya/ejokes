from django.shortcuts import render
import pyjokes

#import jokes

def index(request):
    jokes = pyjokes.get_joke()

    context = {
            'jokes':jokes,
        }

    return render(request, 'index.html', context)