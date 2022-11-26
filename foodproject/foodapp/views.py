from django.http import HttpResponse
from django.shortcuts import render,redirect
from.models import Food
from.forms import FoodForm
# Create your views here.


def index(request):
    food=Food.objects.all()
    context={
        'food_list':food
    }
    return render(request,'index.html',context)
def detail(request,food_id):
    food=Food.objects.get(id=food_id)
    return render(request,"detail.html",{'food':food})
def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        ing= request.POST.get('ing', )
        price = request.POST.get('price', )
        img= request.FILES['img']
        food=Food(name=name,ing=ing,price=price,img=img)
        food.save()
    return render(request,'add.html')
def update(request,id):
    food=Food.objects.get(id=id)
    form=FoodForm(request.POST or None,request.FILES,instance=food)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'food':food})
def delete(request,id):
    if request.method=="POST":
        food=Food.objects.get(id=id)
        food.delete()
        return redirect('/')
    return render(request,"delete.html")