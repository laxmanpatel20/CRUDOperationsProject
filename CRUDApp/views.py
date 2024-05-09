from django.shortcuts import redirect,render
from .models import Member
# Create your views here.

def index(request):
    mem = Member.objects.all()
    dict1 = {'mem':mem}
    return render(request, 'index.html',context=dict1)
def add(request):
    return render(request, 'add.html')
def addrec(request):
    x = request.POST['first']
    y = request.POST['last']
    z = request.POST['country']
    mem = Member(first_name=x, last_name=y, country=z)
    mem.save()
    return redirect("/")
def delete(request,id):
    mem = Member.objects.get(id=id)
    mem.delete()
    return redirect("/")
def update(request,id):
    mem = Member.objects.get(id=id)
    dict1 = {'mem':mem}
    return render(request,'update.html',context=dict1)
def uprecs(request,id):
    x = request.POST['first']
    y = request.POST['last']
    z = request.POST['country']
    mem = Member.objects.get(id=id)
    mem.first_name=x
    mem.last_name=y
    mem.country=z
    mem.save()
    return redirect("/")
