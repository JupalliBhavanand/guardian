from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Employee, Task, OfferLetter, Payroll, Attendance
from django.conf import settings


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']



# Form for Employee to edit their details
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['father_name', 'date_of_birth', 'gender', 'phone', 'email', 'local_address', 'permanent_address', 'photo']
        widgets = {
            'date_of_birth': forms.DateInput(format='%m/%d/%Y', attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        # Set the US date format for displaying and parsing input
        self.fields['date_of_birth'].input_formats = ['%m/%d/%Y']
# Form for Manager to assign a task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to', 'due_date']


# Form for Manager to issue an offer letter

class OfferLetterForm(forms.ModelForm):
    class Meta:
        model = OfferLetter
        fields = ['employee', 'issued_by', 'offer_details', 'file']

class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = ['employee', 'issued_by', 'salary', 'month', 'file']
        widgets = {
            'month': forms.TextInput(attrs={'type': 'month'}),  # HTML5 month input

        }


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['employee', 'date', 'check_in_time', 'check_out_time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # HTML5 date picker
            'check_in_time': forms.TimeInput(attrs={'type': 'time'}),  # HTML5 time picker
            'check_out_time': forms.TimeInput(attrs={'type': 'time'}),  # HTML5 time picker
        }
    def clean(self):
        cleaned_data = super().clean()
        employee = cleaned_data.get('employee')
        date = cleaned_data.get('date')

        if Attendance.objects.filter(employee=employee, date=date).exists():
            raise forms.ValidationError(f"Attendance for {employee} on {date} already exists.")

        return cleaned_data