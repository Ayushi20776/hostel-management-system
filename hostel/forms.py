from django import forms
from .models import Student, Complaint, Fee,Allocation

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = '__all__'

class FeeForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = '__all__'
        from .models import Allocation

class AllocationForm(forms.ModelForm):
    class Meta:
        model = Allocation
        fields = '__all__'