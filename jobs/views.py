from django.shortcuts import render
from .models import job
from django.http import HttpResponse 
# Create your views here.
def home(request):
     

    if request.method == 'POST':
        if request.POST.get('employee_Id') or request.POST.get('complete_ext_id') or request.get.POST('queue') or request.get.POST('role') or request.get.POST('billable_or_non_billable') or request.get.POST('phase')or request.get.POST('function') or request.get.POST('from_date') or request.get.POST('to_date') or request.get.POST('spa') or request.get.POST('leads_ext') or request.get.POST('lead_emp_id')or request.get.POST('manager_ext') or request.get.POST('manager_emp_id') or request.get.POST('l2_ext') or request.get.POST('l2_emp_id') or request.get.POST('workgroup') or request.get.POST('production_type') or request.get.POST('location') or request.get.POST('sub_queue') or request.get.POST('queue_billed') or request.get.POST('days') or request.get.POST('new_sub_queue'):
            assignment_app = job()
            assignment_app.employee_Id = request.get.POST('employee_Id')
            assignment_app.complete_ext_id = request.get.POST('complete_ext_id')
            assignment_app.queue = request.get.POST('queue')
            assignment_app.role = request.get.POST('role')
            assignment_app.billable_or_non_billable = request.get.POST('billable_or_non_billable')
            assignment_app.phase = request.get.POST('phase')
            assignment_app.function = request.get.POST('function')
            assignment_app.from_date = request.get.POST('from_date')
            assignment_app.to_date = request.get.POST('to_date')
            assignment_app.spa = request.get.POST('spa')
            assignment_app.leads_ext = request.get.POST('lead_emp_id')
            assignment_app.manager_ext = request.get.POST('manager_ext')
            assignment_app.manager_emp_id = request.get.POST('manager_emp_id')
            assignment_app.l2_ext = request.get.POST('l2_ext')
            assignment_app.l2_emp_id = request.get.POST('l2_emp_id')
            assignment_app.workgroup = request.get.POST('workgroup')
            assignment_app.production_type = request.get.POST('production_type')
            assignment_app.location = request.get.POST('location')
            assignment_app.sub_queue = request.get.POST('sub_queue')
            assignment_app.queue_billed = request.get.POST('queue_billed')
            assignment_app.days = request.get.POST('days')
            assignment_app.new_sub_queue = request.get.POST('new_sub_queue')
            
            assignment_app.save()

            pass
        else:
            return render(request, 'jobs/form.html')

     
   
    
     

def alldata(request):
    return render(request,'jobs/alldata.html' )