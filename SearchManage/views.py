from django.shortcuts import render

def Mgrsearchview(request):
    return render(request, 'Mgrsearchview.html')

def MgrsearchviewUpdatecase(request):
    return render(request, 'MgrsearchviewUpdatecase.html')

def MgrsearchviewAddcase(request):
    return render(request, 'MgrsearchviewAddcase.html')