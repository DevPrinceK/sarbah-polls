from django.shortcuts import render

from .forms import Voted_listForm
from .models import Floor
from .models import Rep
from .models import Electorate
from .models import Floor
from .models import Voted_list


def base(request):
    # Just for testing the base.html file
    return render(request, 'base.html', {})


def home(request):
    return render(request, 'home.html', {})


def floor(request):
    if request.method == 'POST':
        std_id = request.POST['std_id']  # SUBJECT
        pass_key = request.POST['pass_key']  # BODY

        voter = Electorate.objects.get(pk=pass_key)

        if voter.std_id == std_id:

            # validate electorate

            # Save list of those who logged in
            voted_form = Voted_listForm(request.POST)
            if voted_form.is_valid():
                voted_form.save()
                #
            return render(request, 'floor.html', {})
        else:
            return render()
    else:
        return render(request, 'home.html', {})


def invalid(request):
    return render(request, 'invalid.html', {})


def vote(request):
    if request.method == 'POST':
        return render(request, 'vote.html', {})
    else:
        return render(request, 'home.html', {})


def counter(request):
    if request.method == 'POST':

        return render(request, 'success.html', {})


def ec_login(request):
    return render(request, 'ec_login.html', {})


def ec_admin_result(request):
    return render(request, 'ec_admin_result.html', {})


# class Voted_list(models.Model):
#     std_id = CharField(max_length=8)
#     pass_key = CharField(max_length=100)

#     def __str__(self):
#         return self.id
