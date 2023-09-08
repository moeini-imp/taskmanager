from django.contrib import admin
from .models import Owner,Project,Task,Tags
# Register your models here.
admin.site.register(Owner)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Tags)
