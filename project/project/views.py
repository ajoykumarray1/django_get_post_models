from django.shortcuts import render, HttpResponse

# Create your views here.
def p(request):
    if request.method=="POST":
        n1=request.POST.get("n")
        n2=request.POST.get("d")
        return render(request,"index.html",{'name':n1, 'dep':n2})
    return render(request,"index.html") 
    
def t(request):
    return HttpResponse("hello project test views") 