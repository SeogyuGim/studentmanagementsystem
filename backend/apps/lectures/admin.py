from django.contrib import admin
from .models import Lecture


class LectureAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'lecturer_name',
        'created_datetime',
        'updated_datetime',
    )
    search_fields = ('title', 'lecturer_name')


admin.site.register(Lecture, LectureAdmin)
