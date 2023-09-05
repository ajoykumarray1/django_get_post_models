from django.shortcuts import render, HttpResponse
from .models import Office

# Create your views here.
def home(request):
    if request.method=="POST":
        n1=request.POST.get("n")
        n2=request.POST.get("d")
        info=Office()
        info.name=n1
        info.department=n2
        info.save()
        return render(request,"index.html",{'name':n1, 'dep':n2})
    return render(request,"index.html")
def test(request):
    return HttpResponse("myapp test world")
def m(request):
    return HttpResponse("myapp main root")