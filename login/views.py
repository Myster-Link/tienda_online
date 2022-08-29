from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib import messages

# Create your views here.


def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        nombre = request.POST['first_name']
        apellido = request.POST['last_name']
        password = request.POST['password']

        user = User.objects.create_user(username, email, password)
        user.first_name = nombre
        user.last_name = apellido
        user.save()

        return redirect('login')

    return render(request, 'registration/register.html')
