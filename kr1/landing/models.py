from django.db import models
import json
import datetime
import hashlib


class DataBase:
    def __init__(self):
        self.users = Users()
        self.companies = Companies()
        self.planes = Planes()


class User:
    def __init__(self, id, surname, name, otch, date_of_birth, login, password, group, log):
        self.id = id
        self.surname = surname
        self.name = name
        self.otch = otch
        self.date_of_birth = date_of_birth
        self.login = login
        self.password = password
        self.group = group
        self.log = log

class Users:
    def __init__(self):
        self.path = 'landing/data/users.json'
        self.users = []
        self.load()

    def load(self):
        with open(self.path, 'r', encoding="utf-8") as file:
            text = json.loads(file.read())
        for each in text["users"]: self.users.append(
            User(each["id"], each["surname"], each["name"], each["otch"], each["date_of_birth"], each["login"],
                 each["password"], each["group"], each["log"]))

    def save(self):
        with open(self.path, 'w', encoding="utf-8") as file: json.dump(self.get_list(), file)

    def auth(self, login, password):
        for user in self.users:
            if (user.login == login) and (user.password == password) and (user.log != "Y") : return user
        return None

    def create_users(self, surname, name, otch, date_of_birth, login, password, group, log):
        ids = []
        users = self.get_list()["users"]
        for each in users: ids.append(int(each["id"]))
        if len(ids) == 0:
            users_id = 0
        else:
            users_id = max(ids) + 1
        for each in self.users:
            if login == each.login:
                return False
            else:
                self.users.append(User(users_id, surname, name, otch, date_of_birth, login, password, group, log))
                self.save()
                return True

    def delete_users(self, login):
        for each in self.users:
            if each.login == login:
                self.users.remove(each)
                self.save()
                break

    def lock(self, login, newGroup):
        for each in self.users:
            if each.login == login:
                each.log = newGroup
                self.save()
                return each.log

    def get_list(self):
        data = []
        for each in self.users:
            data.append({"id": each.id, "surname": each.surname, "name": each.name, "otch": each.otch,
                         "date_of_birth": each.date_of_birth, "login": each.login, "password": each.password,
                         "group": each.group,  "log": each.log})
        return {"users": data}



class Plane:
    def __init__(self, id, name, type, age, mest, pilot, dvivatel, prois, comp):
        self.id = id
        self.name = name
        self.type = type
        self.age = age
        self.mest = mest
        self.pilot = pilot
        self.dvivatel = dvivatel
        self.prois = prois
        self.comp = comp


class Planes:
    def __init__(self):
        self.path = 'landing/data/planes.json'
        self.planes = []
        self.load()

    def load(self):
        with open(self.path, 'r', encoding="utf-8") as file:
            text = json.loads(file.read())
        for each in text["planes"]: self.planes.append(
            Plane(each["id"], each["name"], each["type"], each["age"], each["mest"], each["pilot"], each["dvivatel"],
                  each["prois"], each["comp"]))

    def save(self):
        with open(self.path, 'w', encoding="utf-8") as file: json.dump(self.get_list(), file)

    def create_planes(self, name, type, age, mest, pilot, dvivatel, prois, comp):
        ids = []
        planes = self.get_list()["planes"]
        for each in planes: ids.append(int(each["id"]))
        if len(ids) == 0:
            planes_id = 0
        else:
            planes_id = max(ids) + 1
        self.planes.append(Plane(planes_id, name, type, age, mest, pilot, dvivatel, prois, comp))
        self.save()

    def delete_planes(self, name):
        for each in self.planes:
            if each.name == name:
                self.planes.remove(each)
                self.save()
                break

    def get_list(self):
        data = []
        for each in self.planes:
            data.append({"id": each.id, "name": each.name, "type": each.type, "age": each.age, "mest": each.mest,
                         "pilot": each.pilot, "dvivatel": each.dvivatel, "prois": each.prois, "comp": each.comp})
        return {"planes": data}


class Company:
    def __init__(self, id, company, year, location, history, nowadays, boss):
        self.id = id
        self.company = company
        self.year = year
        self.location = location
        self.history = history
        self.nowadays = nowadays
        self.boss = boss


class Companies:
    def __init__(self):
        self.path = 'landing/data/companies.json'
        self.companies = []
        self.load()

    def load(self):
        with open(self.path, 'r', encoding="utf-8") as file:
            text = json.loads(file.read())
        for each in text["companies"]: self.companies.append(
            Company(each["id"], each["company"], each["year"], each["location"], each["history"], each["nowadays"],
                    each["boss"]))

    def save(self):
        with open(self.path, 'w', encoding="utf-8") as file: json.dump(self.get_list(), file)

    def create_companies(self, company, year, location, history, nowadays, boss):
        ids = []
        companies = self.get_list()["companies"]
        for each in companies: ids.append(int(each["id"]))
        if len(ids) == 0:
            company_id = 0
        else:
            company_id = max(ids) + 1
        self.companies.append(Company(company_id, company, year, location, history, nowadays, boss))
        self.save()
        return True

    def delete_companies(self, company):
        for each in self.companies:
            if each.company == company:
                self.companies.remove(each)
                self.save()
                break

    def get_list(self):
        data = []
        for each in self.companies:
            data.append({"id": each.id, "company": each.company, "year": each.year, "location": each.location,
                         "history": each.history, "nowadays": each.nowadays, "boss": each.boss})
        return {"companies": data}
