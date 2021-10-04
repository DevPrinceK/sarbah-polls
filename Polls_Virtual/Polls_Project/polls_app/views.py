from django.shortcuts import render


def base(request):
    # Just for testing the base.html file
    return render(request, 'base.html', {})


def home(request):
    return render(request, 'home.html', {})


def floor(request):
    if request.method == 'POST':
        return render(request, 'floor.html', {})
    else:
        return render(request, 'home.html', {})


def vote(request):
    if request.method == 'POST':
        return render(request, 'vote.html', {})
    else:
        return render(request, 'home.html', {})


def counter(request):
    return render(request, 'success.html', {})


def ec_login(request):
    return render(request, 'ec_login.html', {})


def ec_admin_result(request):
    return render(request, 'ec_admin_result.html', {})
