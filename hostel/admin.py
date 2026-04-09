from django.contrib import admin
from .models import *

admin.site.register(Student)
admin.site.register(Room)
admin.site.register(Allocation)
admin.site.register(Fee)
admin.site.register(Complaint)