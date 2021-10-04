from django.db.models import fields
from django.forms import ModelForm
from .models import Voted_list


class Voted_listForm(ModelForm):
    class Meta():
        model = Voted_list
        fields = ['std_id', 'pass_key']
