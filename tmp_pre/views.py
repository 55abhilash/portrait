from django.shortcuts import render

# Create your views here.

def fn(request):
    print("MADA FAKA!!")
    return render(request, 'tmp.html')
