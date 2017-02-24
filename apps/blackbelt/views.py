from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'blackbelt/index.html')

def register(request):
    if request.method == "GET":
        messages.error(request, 'Nice try, log in or register.')
        return redirect('/')
    user = User.userManager.register(request.POST['firstname'], request.POST['lastname'], request.POST['email'], request.POST['password'], request.POST['passc'])
    if 'errors' in user:
        error = user['errors']
        for msg in error:
             messages.error(request, msg)
        return redirect('/')
    else:
        messages.success(request, 'Successfully registered!')
        User.userManager.create(first_name= user['first_name'], last_name= user['last_name'], email = user['email'], password = user['password'])
        user = User.userManager.filter(email = user['email'])
        request.session['userid'] = user[0].id
    return redirect('/success')

def success(request):
    if 'userid' not in request.session:
        messages.error(request, 'Nice try, log in or register.')
        return redirect('/')
    context = {'user': User.userManager.all(), 'loggeduser': User.userManager.get(id=request.session['userid'])}

    return render(request, 'blackbelt/success.html', context)

def login(request):
    if request.method == "GET":
        messages.error(request, 'Nice try, log in or register.')
        return redirect('/')
    user = User.userManager.login(request.POST['email'], request.POST['password'])
    if 'errors' in user:
        error = user['errors']
        for msg in error:
            messages.error(request, msg)
        return redirect('/')

    else:
        messages.success(request, 'Successfully logged in!')
        user = User.userManager.filter(email = request.POST['email'])
        request.session['userid'] = user[0].id
        return redirect('/success')

def logout(request):
    if 'userid' not in request.session:
        return redirect('/')
    del request.session['userid']
    return redirect('/')

def delete(request, id):
    if 'userid' not in request.session:
        messages.error(request, 'Nice try, log in or register.')
        return redirect('/')
    User.userManager.filter(id=id).delete()
    return redirect('/logout')
def any(request):
    messages.error(request, 'Nice try.')
    return redirect('/')
