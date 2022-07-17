from django.contrib import admin
from .models import Award, Kdrama, Watching
# Register your models here.
admin.site.register(Kdrama)
admin.site.register(Award)
admin.site.register(Watching)