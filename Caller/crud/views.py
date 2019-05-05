# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as RegistredUser
from django.db.models import Q
from django.shortcuts import render

from .models import User


@login_required
def search(request):
    if request.method == 'GET':
        name = request.GET.get('name', -1)
        phone_number = request.GET.get('number', -1)
        spam = request.GET.get('spam', "")
        if name != -1 and phone_number == -1:
            if spam == "":
                users = User.objects.filter(name__contains=str(name))
                return render(request, 'search.html', {'data': users})
            else:
                users = User.objects.filter(name__contains=str(name), spam=spam)
                return render(request, 'search.html', {'data': users})

        if phone_number != -1 and name == -1:
            if spam == "":
                users = User.objects.filter(phone__contains=str(phone_number))
                return render(request, 'search.html', {'data': users})

            else:
                users = User.objects.filter(phone__contains=str(phone_number), spam=spam)
                return render(request, 'search.html', {'data': users})

        if name == -1 and phone_number == -1:
            if spam == "":
                users = User.objects.all()
                return render(request, 'search.html', {'data': users})

            else:
                users = User.objects.filter(spam=spam)
                return render(request, 'search.html', {'data': users})

        else:
            if spam == "":
                users = User.objects.filter(Q(name__contains=name) | Q(phone__contains=str(phone_number)))
                return render(request, 'search.html', {'data': users})

            else:
                users = User.objects.filter(Q(name__contains=name) | Q(phone__contains=str(phone_number)), spam=spam)
                return render(request, 'search.html', {'data': users})


@login_required
def spam(request, number):
    if request.method == 'GET':
        user = User.objects.filter(phone=number)
        try:
            registreduser = RegistredUser.signupform.get(phone=number)
        except:
            for udetail in user:
                udetail.spam = True
                udetail.save()
        return render(request, 'spam.html', {'data': user})


def home(request):
    users = User.objects.all()
    return render(request, 'home.html', {'data': users})
