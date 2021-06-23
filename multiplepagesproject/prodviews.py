from django.http import HttpResponse
from django.shortcuts import render
from multiplepagesproject.prodmodels import proddisplay
from multiplepagesproject.catmodels import catdisplay
from multiplepagesproject.prodforms import productforms
from django.contrib import messages
from django.core.paginator import Paginator

def showprod(request):
    result = proddisplay.objects.all()
    paginator = Paginator(result, 3)
    page = request.GET.get('page')
    result = paginator.get_page(page)
    return render(request, 'product/productdetails.html', {'proddisplay':result})

def delrecprod(request,id):
    delproduct = proddisplay.objects.get(id=id)
    delproduct.delete()
    result = proddisplay.objects.all()
    return render(request, 'product/productdetails.html', {'proddisplay': result})


def editprod(request, id):
    displayclient = proddisplay.objects.get(id=id)
    return render(request, "product/productedit.html", {"proddisplay": displayclient})

def updateprod(request, id):
    updateclient = proddisplay.objects.get(id=id)
    form = productforms(request.POST, instance=updateclient)
    if form.is_valid:
        form.save()
        messages.success(request, "Record Updated Successfully...!")
        return render(request, "product/productedit.html", {"proddisplay": updateclient})

def showcatname(request):
    result = catdisplay.objects.all()
    return render(request, 'product/productinsert.html', {'rc': result})

"""def upd(request):
    #se = proddisplay.objects.get('categoryid')
    se = proddisplay.objects.all()
    rek=se['categoryid']
    print(rek)
    return render(request,'product/productinsert.html',{'rmm':rek})

    for p in proddisplay.objects.raw('SELECT id FROM product'):
        print(p)
        return render(request, 'product/productinsert.html', {'rc': p})

    sw= proddisplay.objects.filter('pname')
    print(sw)
    return render(request, 'product/productinsert.html', {'rc': sw})"""



def insertprod(request):
    if request.method == "POST":
        if request.POST.get('categoryid')and request.POST.get('pprice')and request.POST.get('pcontent')and request.POST.get('pimage')and request.POST.get('pdisplayorder')and request.POST.get('pstatus'):
            saverecordpd = proddisplay()
            saverecordpd.categoryid = request.POST.get('categoryid')
            #saverecordpd.pname = request.POST.get('pname')
            saverecordpd.pprice = request.POST.get('pprice')
            saverecordpd.pcontent = request.POST.get('pcontent')
            saverecordpd.pimage = request.POST.get('pimage')
            saverecordpd.pdisplayorder = request.POST.get('pdisplayorder')
            saverecordpd.pstatus = request.POST.get('pstatus')
            saverecordpd.save()
            messages.success(request, 'Record Saved Successfully...!')
            return render(request, 'product/productinsert.html')
    else:
            messages.success(request, 'Record not saved Successfully...!')
            #print(request.POST.get('pprice'))
            return render(request, 'product/productinsert.html')