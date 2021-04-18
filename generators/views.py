from django.shortcuts import render
import random
import string

# Create your views here.


def index(request):
    return render(request, 'generators/index.html')


def about(request):
    return render(request, 'generators/about.html')


def password(request):
    thepassword = ''
    char_set = string.ascii_lowercase
    if request.GET.get('uppercase'):
        char_set += string.ascii_uppercase
    if request.GET.get('number'):
        char_set += string.digits
    special = '!@#$%^&*()'
    if request.GET.get('special'):
        char_set += special

    length = int(request.GET.get('length'))
    for i in range(length):
        thepassword += random.choice(char_set)
    return render(request, 'generators/password.html', {'password': thepassword})
