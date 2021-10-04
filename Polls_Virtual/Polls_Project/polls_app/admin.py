from django.contrib import admin

from .models import Floor
from .models import Rep
from .models import Electorate

admin.site.register(Floor)
admin.site.register(Rep)
admin.site.register(Electorate)
