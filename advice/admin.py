from django.contrib import admin
from .models import *


class MuscleAdmin(admin.ModelAdmin):
    list_display = ["name", "function"]
    list_editable = ["function"]


class ExercisesAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    list_editable = ["description"]


class ClientAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "target", "phone", "data"]
    list_editable = ["last_name", "target", "phone"]
    list_per_page = 10
    search_fields = ["first_name", "last_name"]


admin.site.register(Muscle, MuscleAdmin)
admin.site.register(Exercises, ExercisesAdmin)
admin.site.register(Client, ClientAdmin)