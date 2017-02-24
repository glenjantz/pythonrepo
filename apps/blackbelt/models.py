from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
Email_Regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
Name_Regex = re.compile(r'^[A-Za-z]+$')


class UserManager(models.Manager):
    def register(self, postFirstName, postLastName, postEmail, postPassword, postConfirm):
        status = True
        errorlist = []
        if not Email_Regex.match(postEmail):
            errorlist.append('Invalid email!')
            status = False
            # return {'errors':'False'}
        if len(User.userManager.filter(email = postEmail)) > 0:
            errorlist.append('Email already exists, please log in.')
            status = False
            # return {'errors1': 'False'}
        if postPassword != postConfirm:
            errorlist.append('Passwords must match.')
            status = False
            # return {'errors2': 'False'}
        if len(postFirstName) < 2:
            errorlist.append('First name must be at least 2 characters.')
            status = False
            # return {'errors3': 'False'}
        elif not Name_Regex.match(postFirstName):
            errorlist.append('First name can not contain numbers.')
            status = False
        if len(postLastName) < 2:
            errorlist.append('Last name must be at least 2 characters.')
            status = False
            # return {'errors3': 'False'}
            # return {'errors4': 'False'}
        elif not Name_Regex.match(postLastName):
            errorlist.append('Last name can not contain numbers.')
            status = False
            # return {'errors4': 'False'}
        if len(postPassword) < 8:
            errorlist.append('Password must be greater than 8 characters')
            status = False
            # return {'errors5': 'False'}
        if status == False:
            return {'errors': errorlist}
        else:
            password = postPassword
            hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            return {'first_name': postFirstName, 'last_name': postLastName, 'email': postEmail, 'password': hashed}

    def login(self, postEmail, postPassword):
        status = True
        errorlist = []
        user = User.userManager.filter(email = postEmail)
        if len(postEmail) < 1:
            status = False
            errorlist.append('Must fill in email.')
            # return {'errors': 'False'}
        if len(postPassword) < 1:
            status = False
            errorlist.append('Must fill in password.')
            # return {'errors5': 'False'}
        if len(user) < 1:
            status = False
            errorlist.append('Email does not exist, please register.')
            # return {'errors6': 'False'}
        if status == False:
            return {'errors': errorlist}
        else:
            if bcrypt.hashpw(postPassword.encode(), user[0].password.encode()) == user[0].password:
                return {'login': 'true'}
            else:
                status = False
                errorlist.append('Password does not match records.')
                return {'errors': errorlist}
                # {'errors': 'False'}

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    userManager = UserManager()
