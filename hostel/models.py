from django.db import models

# Student Table
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name


# Room Table
class Room(models.Model):
    room_number = models.IntegerField()
    capacity = models.IntegerField()
    available_beds = models.IntegerField()

    def __str__(self):
        return f"Room {self.room_number}"


# Allocation (Student + Room connect)
class Allocation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    bed_number = models.IntegerField()

    def __str__(self):
        return f"{self.student} -> Room {self.room.room_number}"


# Fee Management
class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.IntegerField()
    payment_method = models.CharField(max_length=20, default="UPI")  # 👈 add
    paid = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
# Complaint System
class Complaint(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return f"{self.student} - {self.status}"