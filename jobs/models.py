from django.db import models

# Create your models here.
class job(models.Model):
    employee_Id = models.CharField(max_length=200)
    complete_ext_id = models.CharField(max_length=200)
    queue = models.CharField(max_length=200)
    role  = models.CharField(max_length=200)
    billable_or_non_billable = models.CharField(max_length=200)
    phase = models.CharField(max_length=200)
    function = models.CharField(max_length=200)
    from_date = models.CharField(max_length=200)
    to_date = models.CharField(max_length=200)
    spa = models.CharField(max_length=200)
    leads_ext = models.CharField(max_length=200)
    lead_emp_id = models.CharField(max_length=200)
    manager_ext = models.CharField(max_length=200)
    manager_emp_id = models.CharField(max_length=200)
    l2_ext =  models.CharField(max_length=200)
    l2_emp_id= models.CharField(max_length=200)
    workgroup = models.CharField(max_length=200)
    production_type = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    sub_queue = models.CharField(max_length=200)
    queue_billed = models.CharField(max_length=200)
    days = models.CharField(max_length=50)
    new_sub_queue = models.CharField(max_length=200)

    from django.forms import ModelForm

class Meta:
    db_table = "job"


