from django import forms
from .models import *

class LoginForm(forms.Form):
    login = forms.CharField(label="Логин", required=True, widget=forms.TextInput(attrs={'placeholder': "Введите ваш логин..."}), max_length=50)
    password = forms.CharField(label="Пароль", required=True, widget=forms.PasswordInput(attrs={'placeholder': "Введите ваш пароль..."}), max_length=150)


class CreationForm(forms.Form):
    surname = forms.CharField(label="Фамилия", required=True, widget = forms.TextInput(attrs={'placeholder': "Фамилия пользователя..."}), max_length=150)
    name = forms.CharField(label="Имя", required=True, widget = forms.TextInput(attrs={'placeholder': "Имя пользователя..."}), max_length=150)
    otch = forms.CharField(label="Отчество", required=True, widget = forms.TextInput(attrs={'placeholder': "Отчество пользователя..."}), max_length=150)
    date_of_birth= forms.CharField(label="Дата рождения", required=True, widget = forms.TextInput(attrs={'placeholder': "Дата рождения пользователя в формате ДД.ММ.ГГГГ..."}), max_length=150)
    login = forms.CharField(label="Логин", required=True, widget=forms.TextInput(attrs={'placeholder': "Логин пользователя..."}), max_length=50)
    password = forms.CharField(label="Пароль", required=True, widget=forms.PasswordInput(attrs={'placeholder': "Пароь пользователя..."}), max_length=50)
    group = forms.ChoiceField(label="Группа бзопасности", widget=forms.Select(), choices=([('user', 'user'), ('boss', 'boss'), ('moder', 'moder'), ]), required=True)
    log = forms.ChoiceField(label="Доступ(1-заблокирован)", widget=forms.Select(), choices=([('0', '0'),('1','1'),]), required=True)


class NewCompany(forms.Form):
    company = forms.CharField(label="Название", required=True, max_length=50, widget=forms.TextInput(attrs={'placeholder': "Название компании..."}))
    year = forms.CharField(label="Год основания", required=True, max_length=50, widget=forms.TextInput(attrs={'placeholder': "Год основания компании..."}))
    location = forms.CharField(label="Местоположение", max_length = 500, required=True, widget=forms.TextInput(attrs={'placeholder': "Введите полный адрес компании..."}))
    history = forms.CharField(label="История", required=True, max_length=500, widget=forms.TextInput(attrs={'placeholder': "История возникновения компании..."}))
    nowadays = forms.CharField(label="Наше время", required=True, max_length=500, widget=forms.TextInput(attrs={'placeholder': "Что из себя предствавляет компания на сегодняшний день..."}))
    boss = forms.CharField(label="Директор", required=True, max_length=50, widget=forms.TextInput(attrs={'placeholder': "ФИО директора компании,(с какого года занимает пост)..."}))

class NewPlane(forms.Form):
    name = forms.CharField(label="Название", required=True, max_length=150, widget=forms.TextInput( attrs={'placeholder': "Полное название самолета..."}))
    type = forms.CharField(label="Тип", required=True, max_length=150, widget=forms.TextInput( attrs={'placeholder': "Тип самолета..."}))
    age = forms.CharField(label="Год покупки", required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': "Год покупки в формате:'Приобретен в ... году'..."}))
    mest = forms.CharField(label="Мест", required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': "Количетво мест в самолете..."}))
    pilot = forms.CharField(label="Пилот", required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': "ФИО пилота самолета..."}))
    dvivatel = forms.CharField(label="Двигатель", required=True, max_length=150,  widget=forms.TextInput(attrs={'placeholder': "Модель/-ли двигателя/-лей самолета..."}))
    prois = forms.CharField(label="Производство", required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': "Название компании-производителя самолета..."}))
    comp = forms.CharField(label="Компания", required=True, max_length=150, widget=forms.TextInput( attrs={'placeholder': "Название компании, владельца самолета..."}))
