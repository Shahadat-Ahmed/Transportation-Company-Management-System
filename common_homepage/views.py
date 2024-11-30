from django.shortcuts import render

def homepage(request):
    return render(request, 'common_homepage.html')
