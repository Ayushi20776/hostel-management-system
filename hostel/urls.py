from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('students/', student_list),

    path('add-student/', add_student),
    path('add-complaint/', add_complaint),
    path('add-fee/', add_fee),
    path('allocate-room/', allocate_room),

    path('receipt/<int:id>/', receipt),

    path('register/', register),
    path('login/', user_login),
    path('logout/', user_logout),
]