from django.shortcuts import render

def searchView(request):
    return render(request, 'Searchview.html')
