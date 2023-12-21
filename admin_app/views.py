from django.shortcuts import render
from advbook_app.models import *

def data(request):
    return render(request,'data.html')

def admin1(request):
    advocate_count= Adv_Register.objects.filter(approval = 'Approved').count()
    user_count= Register.objects.all().count()
    appointment_count = Appointment.objects.filter(status = 'Accepted').count()
    context = {
        'advocate_count':advocate_count ,
        'user_count' : user_count ,
        'appointment_count' : appointment_count ,
    }

    return render(request,'admin1.html',context)

def view_user_details(request):
    var=Register.objects.all()
    context = {
        'var':var
    }
    return render(request,'view_user_details.html',context)

def view_adv_details(request):
    var=Adv_Register.objects.filter(approval = "waiting for approval")
    context = {
        'var' : var
    }
    return render(request,'view_adv_details.html',context)

def approve_admin(request, advocate_id):
    Adv_Register.objects.filter(id = advocate_id).update(
        approval = "Approved"
    )
    return render(request,'view_adv_details.html')

def reject_admin(request, advocate_id):
    Adv_Register.objects.filter(id= advocate_id).update(
        approval  = "Rejected"
    )
    return render(request,'view_user_details.html')

def view_approved_adv(request):
    var=Adv_Register.objects.filter(approval = "Approved")
    context = {
        'var' : var
    }
    return render(request,'approved.html',context)
    
def view_rejected_adv(request):
    var=Adv_Register.objects.filter(approval = "Rejected")
    context = {
        'var' : var
    }
    return render(request,'rejected.html',context)

