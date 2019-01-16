from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.context_processors import csrf
from .models import *
from .forms import *

import json

def current_user(sess, request):
    sess['user_login']=request.session['user_login']
    sess['user_group'] = request.session['user_group']


def home(request):
    session = {}
    with open('landing/data/companies.json', 'r', encoding='utf8') as file:
        text = json.loads(file.read())
    with open('landing/data/planes.json', 'r', encoding='utf8') as file:
        kext = json.loads(file.read())
    data = text["companies"]
    vata = kext["planes"]
    try:
        current_user(session, request)
    except:
        print("error")
        return redirect('auth')
    session['title'] = 'Авиакомпании'
    session['companies'] = data
    session['planes'] = vata
    return render(request, 'main/home.html', session)


def chr (request):
    session = {}
    try:
        current_user(session, request)
    except:
        print("We've got a bad news, sir")
        return redirect('auth')
    session['title'] = 'Управления авиакомпаниями'
    data = DataBase()
    companies = data.companies.get_list()
    session["companies"] = companies["companies"]
    if request.method == "POST":
        form = NewCompany(request.POST)
        if "delete" in request.POST.keys():
            data.companies.delete_companies(request.POST['delete'])
            session = data.companies.get_list()
        elif "save" in request.POST.keys():
            data.companies.create_companies(request.POST['company'], request.POST['year'], request.POST['location'], request.POST['history'], request.POST['nowadays'], request.POST['boss'])
            session = data.companies.get_list()
    else:
        form = NewCompany()
    session = data.companies.get_list()
    session['title'] = 'Управление авиакомпаниями'
    try:
        current_user(session, request)
    except:
        print("Sounds bad!")
    session['form'] = form
    return render(request, 'main/changeCompany.html', session)

def user(request):
    session = {}
    with open("landing/data/users.json", "r", encoding="utf8") as file:
        text = json.loads(file.read())
    data = text["user"]
    try:
        current_user(session, request)
    except:
        print("error")
        return redirect('auth')
    session['title'] = 'Пользователи'
    session['user'] = data
    return render(request, 'main/changeUser.html', session)

def chuser(request):
    session = {}
    try:
        current_user(session, request)
    except:
        print("We've got a bad news, sir")
        return redirect('auth')
    session['title'] = 'Пользователи'

    data = DataBase()
    users = data.users.get_list()
    session["users"] = users["users"]
    if request.method == "POST":
        form = CreationForm(request.POST)
        if "delete" in request.POST.keys():
            data.users.delete_users(int(request.POST['delete']))
            session = data.users.get_list()
        elif "save" in request.POST.keys():
            data.users.create_users( request.POST['surname'], request.POST['name'], request.POST['otch'], request.POST['date_of_birth'], request.POST['login'], request.POST['password'], request.POST['group'], request.POST['log'])
            session = data.users.get_list()
        elif "lock" in request.POST.keys():
            user_update = request.POST.get("lock")
            data.users.lock(user_update, "1")
        elif "unlock" in request.POST.keys():
            user_update = request.POST.get("unlock")
            data.users.lock(user_update, "0")
    else:
        form = CreationForm()
    session = data.users.get_list()
    session['title'] = 'Пользователи'
    try:
        current_user(session, request)
    except:
        print("Sounds bad!")
    session['form'] = form
    return render(request, 'main/changeUser.html', session)




def planes(request):
    session = {}
    with open("landing/data/planes.json", "r", encoding="utf8") as file:
        text = json.loads(file.read())
    data = text["planes"]
    try:
        current_user(session, request)
    except:
        print("error")
        return redirect ('auth')
    session['title'] = 'Авиапарк'
    session['planes'] = data
    return render(request, 'main/planes.html', session)


def chplane (request):
    session = {}
    try:
        current_user(session, request)
    except:
        print("We've got a bad news, sir")
        return redirect('auth')
    session['title'] = 'Управление авиапарком'

    data = DataBase()
    planes = data.planes.get_list()
    session["planes"] = planes["planes"]
    if request.method == "POST":
        form = NewPlane(request.POST)
        if "delete" in request.POST.keys():
            data.planes.delete_planes(request.POST['delete'])
            session = data.planes.get_list()
        elif "save" in request.POST.keys():
            data.planes.create_planes(request.POST['name'], request.POST['type'], request.POST['age'],request.POST['mest'], request.POST['pilot'], request.POST['dvivatel'],request.POST['prois'] ,request.POST['comp'])
            session = data.planes.get_list()

    else:
        form = NewPlane()
    session = data.planes.get_list()
    session['title'] = 'Управление авипарком'
    try:
        current_user(session, request)
    except:
        print("Sounds bad!")
    session['form'] = form
    return render(request, 'main/changePlane.html', session)

def auth(request):
    data = DataBase()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user_login = request.POST['login']
            user_pass = request.POST['password']
            current_u = data.users.auth(user_login, user_pass)
            try:
                if current_u.group:
                    request.session['user_login'] = current_u.login
                    request.session['user_group'] = current_u.group
                    return redirect('home')
            except:
                messages.error(request, f'Неверный логин и/или пароль!... возможно вы себя плохо вели и вас заблокировали)))')
        else: print("invalid form;(")
    else:
        try:
            if request.session['user_login:']: return redirect('home')
        except: form = LoginForm()
    return render(request, 'main/auth.html', {'form': form, 'title': 'Авторизация'})




def exit(request):
	request.session.clear()
	return redirect('auth')