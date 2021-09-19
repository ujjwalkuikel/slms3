from courses.models import Lesson, Standard
from django.contrib import admin
from courses.models import Standard,Subject,Lesson



# Register your models here.
admin.site.register(Standard)
admin.site.register(Subject)
admin.site.register(Lesson)