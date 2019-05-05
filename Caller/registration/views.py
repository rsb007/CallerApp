# Create your views here.
import json
import random
from collections import namedtuple

from django.apps import apps
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import SignUpForm


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_list = []
            appdata = apps.get_model('crud', 'User')
            with open('/home/rahul/Downloads/random.json') as json_file:
                user_list = json.load(json_file, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

            temp_data = random.choices(user_list, k=5)

            for user_data in temp_data:
                u = appdata(name=user_data.name, email=user_data.email,
                            phone=user_data.phone)
                u.save()

            appdb = appdata(name=form.cleaned_data['name'], email=form.cleaned_data['email'],
                            phone=form.cleaned_data['phone'])
            appdb.save()
            appdb = appdata.objects.all()
            auth_login(request, user)
            return redirect('/', {'data': appdb})
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
