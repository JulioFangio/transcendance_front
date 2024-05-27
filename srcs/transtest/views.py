from datetime import datetime
from django.shortcuts import render

def homepage(request):
    return render(request, "homepage.html", context={"date": datetime.today()})

def userpage(request):
    return render(request, "userpage.html", context={"date": datetime.today()})
#Le fair de rajouter un context permet de passer des variables a la page html
# pour ensuite les inserer dans le code html grace a la syntaxe {{ nom_de_la_variable }}
# cela sera particulierement utilse lorsqu il faudra aller chercher des variables contenues
# dans la base de donnees pour les afficher dans la page web.

def log_in(request):
    return render(request, "log_in.html", context={"date": datetime.today()})

def sign_up_page(request):
    return render(request, "sign_up.html", context={"date": datetime.today()})

def sign_up_form_page(request):
    return render(request, "sign_up_form.html", context={"date": datetime.today()})