"""multiplepagesproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import homeviews
from . import catviews
from . import pgeviews
from . import prodviews


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', homeviews.homepage, name='homepage'),

    path('categorydetails', catviews.showcat, name='showcat'),
    path('delete/<int:id>', catviews.delreccat),
    path('edit/<int:id>', catviews.editcat),
    path('update/<int:id>', catviews.updatecat),
    path('categoryinsert', catviews.insertcat, name='insertcat'),
    #path('categorydetails', catviews.tablecat, name='tablecat'),

    path('pagesdetails', pgeviews.showpge, name='showpge'),
    path('delete2/<int:id>', pgeviews.delrecpge),
    path('edit2/<int:id>', pgeviews.editpge),
    path('update2/<int:id>', pgeviews.updatepge),
    path('pagesinsert', pgeviews.insertpge, name='insertpge'),

    path('productdetails', prodviews.showprod, name='showprod'),
    path('productinsert', prodviews.showcatname),
    path('delete3/<int:id>', prodviews.delrecprod),
    path('edit3/<int:id>', prodviews.editprod),
    path('update3/<int:id>', prodviews.updateprod),
    path('productinsert', prodviews.insertprod, name='insertprod'),
]

