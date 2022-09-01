
from django.contrib import admin
from django.urls import path
from pdf import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.akceptuj,name="akcpetuj"),
    path("<int:id>/",views.kontynuuj,name='kontynuuj'),
    path('list/',views.lista,name='lsita'),
]
