from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
import bcrypt

def uni_to_str(mydict):
    data = {}
    for key, val in mydict.iteritems():
        data[key] = str(val)
    return data

class UserManager(models.Manager):
    def createUser(self,form):
        flag = False
        errors = {}
        data = uni_to_str(form)

        if len(data['name']) < 5:
            errors['name'] = "Name must be greater than 5 characters"
            flag = True

        if len(data['alias']) < 3:
            errors['alias']= "Alias must be longer than 3 characters!"
            flag = True
        if len(data['password']) < 8:
            flag = True
            errors['password'] = "Password must be at least 8 characters"

        if flag:
            return (False, errors)

        new_user = self.create(name=data['name'], alias=data['alias'], email=data['email'], password=bcrypt.hashpw(data['password'], bcrypt.gensalt()))

        return (True, new_user)

    def login(self, form):
        flag = False
        errors = {}
        data = uni_to_str(form)

        try:
            user = User.manager.get(email=data['email'])
        except Exception:
            errors['email'] = "email not found in database"
            return (False, errors)
        if not bcrypt.checkpw(data['password'],user.password.encode()):
            flag = True
            errors['password'] = "Invalid credentials"
        if flag:
            return (False,errors)
        return (True,user)


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manager = UserManager()
    def __repr__(self):
        return "this object contains: {} {}, {} - {}".format(self.name, self.alias, self.email, self.id)
