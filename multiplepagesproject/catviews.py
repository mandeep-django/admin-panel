from django.http import HttpResponse
from django.shortcuts import render
from multiplepagesproject.catmodels import catdisplay
from multiplepagesproject.catforms import categoryforms
from django.contrib import messages
from django.core.paginator import Paginator

def showcat(request):
    result = catdisplay.objects.all()
    paginator = Paginator(result, 3)
    page = request.GET.get('page')
    result = paginator.get_page(page)
    return render(request, 'category/categorydetails.html', {"catdisplay":result})

def delreccat(request,id):
    delcategory = catdisplay.objects.get(id=id)
    delcategory.delete()
    result = catdisplay.objects.all()
    return render(request, 'category/categorydetails.html', {'catdisplay': result})


def editcat(request, id):
    displayclient = catdisplay.objects.get(id=id)
    return render(request, "category/categoryedit.html", {"catdisplay": displayclient})

def updatecat(request,id):
    updateclient = catdisplay.objects.get(id=id)
    form = categoryforms(request.POST, instance=updateclient)
    if form.is_valid:
        form.save()
        messages.success(request, "Record Updated Successfully...!")
        return render(request, "category/categoryedit.html", {"catdisplay": updateclient})


def insertcat(request):
    if request.method == "POST":
        if request.POST.get('catname')and request.POST.get('displayorder')and request.POST.get('status'):
            saverecord = catdisplay()
            saverecord.catname = request.POST.get('catname')
            saverecord.displayorder = request.POST.get('displayorder')
            saverecord.status = request.POST.get('status')
            saverecord.save()
            messages.success(request, 'Record Saved Successfully...!')
            return render(request, 'category/categoryinsert.html')
    else:
            return render(request, 'category/categoryinsert.html')


def tablecat(request):
    result = catdisplay.objects.all()
    paginator = Paginator(result,3)
    page = request.GET.get('page')
    result = paginator.get_page(page)
    return render( request, 'category/categorydetails.html', {'catdisplay':result})