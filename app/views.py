from django.shortcuts import render

# Create your views here.

def forloop(request):
    d={'name':'anand'}
    return render(request,'forloop.html',d)

def forloop2(request):
    d={'age':[21]}
    return render(request,'forloop2.html',d)
