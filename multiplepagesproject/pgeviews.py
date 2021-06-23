from django.http import HttpResponse
from django.shortcuts import render
from multiplepagesproject.pgemodels import pgedisplay
from multiplepagesproject.pgeforms import pagesforms
from django.contrib import messages
from django.core.paginator import Paginator

def showpge(request):
    result = pgedisplay.objects.all()
    paginator = Paginator(result, 3)
    page = request.GET.get('page')
    result = paginator.get_page(page)
    return render(request, 'pages/pagesdetails.html', {'pgedisplay':result})


def delrecpge(request,id):
    delpage = pgedisplay.objects.get(id=id)
    delpage.delete()
    result = pgedisplay.objects.all()
    return render(request, 'pages/pagesdetails.html', {'pgedisplay': result})


def editpge(request, id):
    displayclient = pgedisplay.objects.get(id=id)
    return render(request, "pages/pagesedit.html", {"pgedisplay": displayclient})

def updatepge(request,id):
    updateclient = pgedisplay.objects.get(id=id)
    form = pagesforms(request.POST, instance=updateclient)
    if form.is_valid:
        form.save()
        messages.success(request, "Record Updated Successfully...!")
        return render(request, "pages/pagesedit.html", {"pgedisplay": updateclient})


def insertpge(request):
    if request.method == "POST":
        if request.POST.get('name')and request.POST.get('content')and request.POST.get('displayorder')and request.POST.get('status'):
            saverecordpg = pgedisplay()
            saverecordpg.name = request.POST.get('name')
            saverecordpg.content = request.POST.get('content')
            saverecordpg.displayorder = request.POST.get('displayorder')
            saverecordpg.status = request.POST.get('status')
            saverecordpg.save()
            messages.success(request, 'Record Saved Successfully...!')
            return render(request, 'pages/pagesinsert.html')
    else:
            return render(request, 'pages/pagesinsert.html')
