from django import forms  
from jobs.models import job  
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = job  
        fields = "__all__"  