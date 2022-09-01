from django.shortcuts import render
from .models import Profil
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

def akceptuj(request):
    if request.method =="POST":
        imie = request.POST.get("imie","")
        nazwisko = request.POST.get("nazwisko","")
        email = request.POST.get("email","")
        nr_telefonu=request.POST.get("nr_telefonu","")
        informacje_ogolne=request.POST.get("informacje_ogolne","")
        wyksztalcenie=request.POST.get("wyksztalcenie","")
        szkola=request.POST.get("szkola_srednia","")
        uniwersytet=request.POST.get("uniwersytet","")
        doswiadczenie=request.POST.get("doswiadczenie","")
        umiejetnosci=request.POST.get("umiejetnosci","")           #zbieramy dane z metody post

        profil = Profil(imie=imie, nazwisko=nazwisko, email=email, nr_telefonu=nr_telefonu, informacje_ogolne= informacje_ogolne,
                        wyksztalcenie=wyksztalcenie, szkola= szkola, uniwersytet=uniwersytet, doswiadczenie=doswiadczenie,
                        umiejetnosci=umiejetnosci)   #tworzymy obiekt klasy Profil
        profil.save() #zapisujmey w bazie danych

    return render(request,'pdf/akceptuj.html')

def kontynuuj(request,id):
    user_profile = Profil.objects.get(pk=id)
    template = loader.get_template('pdf/kontynuuj.html')
    html = template.render({'user_profile':user_profile})
    options={
        'page-size':'Letter',
        'encoding':"UTF-8",
    }
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    pdf = pdfkit.from_string(html, False, options, configuration=config )
    response = HttpResponse(pdf, content_type='application/pdf')
    response["Content-Disposition"] = 'attachment'
    filename = 'resume.pdf'
            #konwersja html na pdf za pomoca pdfkit
    return response

def lista(request):
    profil = Profil.objects.all()
    return render(request,'pdf/lista.html',{'profil':profil})   #lista stworzonych cv z opcja pobrania