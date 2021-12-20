from django.shortcuts import render

def Druginfolist(request):
    return render(request, 'Druginfolist.html')
def Druginfoview(request):
    return render(request, 'Druginfoview.html')