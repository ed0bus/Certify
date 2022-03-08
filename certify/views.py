from django.shortcuts import render
from django.views.decorators.cache import cache_page


@cache_page(60*60, key_prefix='home')
def home(request):
    return render(request, 'home.html')

