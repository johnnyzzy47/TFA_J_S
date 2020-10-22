from django.http import HttpResponse
from django.shortcuts import render,redirect
  
from .models import Squirrel
from .forms import SquirrelForm


def edit_squirrel(request,UID):
    squirrel= Squirrel.objects.get(UID=UID)
    if request.method =='POST':
        form = SquirrelForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SquirrelForm(instance=squirrel)
    context ={
            'form':form,
             }
    return render(request, 'tracker_app/edit.html', context)

def add_squirrel(request):
    if request.method == "POST":
        form= SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SquirrelForm()
    context ={
            'form':form,
        }
    return render(request,'tracker_app/edit.html',context)

def map_squirrel(request):
    sightings= Squirrel.objects.all()[:100]
    context ={
            'sightings':sightings,
             }
    return render(request, 'tracker_app/map.html', context)

def sighting(request):
    squirrel = Squirrel.objects.all()
    context = {
            'squirrels': squirrel,
        }
    return render(request, 'tracker_app/sightings.html',context)

def main(request):
    return render(request, 'tracker_app/main.html')  

def get_stats(request):
    #squirrel= Squirrel.objects.all()
    AM_count = 0
    PM_count = 0
    Kuks_count =0
    Quaas_count =0
    Moans_count =0
    Foraging_count =0
    for i in Squirrel.objects.all():
        if i.Shift == 'AM':
            AM_count+=1
        if i.Shift == 'PM':
            PM_count+=1
        if i.Kuks == True:
            Kuks_count +=1
        if i.Quaas== True:
            Quaas_count +=1
        if i.Moans == True:
            Moans_count +=1
        if i.Foraging == True:
            Foraging_count +=1
    context = {
            'AM_count':AM_count,
            'PM_count':PM_count,
            'Kuks_count':Kuks_count,
            'Quaas_count':Quaas_count,
            'Foraging_count':Foraging_count,
            'Moans_count':Moans_count,
            }
    return render(request, 'tracker_app/stats.html', context)

# Create your views here.
