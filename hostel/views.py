from django.shortcuts import render, redirect
from .models import Student, Fee,Room,Complaint
from .forms import StudentForm, ComplaintForm, FeeForm, AllocationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# 🔹 HOME
def home(request):
    total_students = Student.objects.count()
    total_rooms = Room.objects.count()
    total_complaints = Complaint.objects.count()
    total_fees = Fee.objects.count()

    context = {
        'students': total_students,
        'rooms': total_rooms,
        'complaints': total_complaints,
        'fees': total_fees,
    }

    return render(request, 'home.html', context)


# 🔹 STUDENT LIST
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


# 🔹 ADD STUDENT
def add_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'add_student.html', {'form': form})


# 🔹 COMPLAINT
def add_complaint(request):
    form = ComplaintForm()
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'add_complaint.html', {'form': form})


# 🔹 FEE
def add_fee(request):
    if request.method == 'POST':
        form = FeeForm(request.POST)
        if form.is_valid():
            fee = form.save()
            return redirect(f'/receipt/{fee.id}/')
    else:
        form = FeeForm()

    return render(request, 'add_fee.html', {'form': form})


# 🔹 RECEIPT
def receipt(request, id):
    fee = Fee.objects.get(id=id)
    return render(request, 'receipt.html', {'fee': fee})


# 🔹 ROOM ALLOCATION
def allocate_room(request):
    form = AllocationForm()
    if request.method == 'POST':
        form = AllocationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'allocate_room.html', {'form': form})


# 🔹 REGISTER
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(username=username, password=password)
        return redirect('/login/')

    return render(request, 'register.html')


# 🔹 LOGIN
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid Credentials'})

    return render(request, 'login.html')


# 🔹 LOGOUT
def user_logout(request):
    logout(request)
    return redirect('/login/')