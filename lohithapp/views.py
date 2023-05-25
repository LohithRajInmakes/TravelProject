from django.shortcuts import render
from django.http import HttpResponse
from .models import Place
from .models import Person

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    player=Person.objects.all()
    return render(request, 'index.html',{'result':obj,'data':player})







# def addition(request):
#     firstnumber=int(request.GET['num1'])
#     secondnumber=int(request.GET['num2'])
#     answer=firstnumber+secondnumber
#     return render(request,'addition.html',{'result':answer})

# def abort(request):
#     return render(request,'abort.html')
#
# def close(request):
#     return HttpResponse("hi close it")