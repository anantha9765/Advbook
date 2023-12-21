from django.shortcuts import render,redirect
from .models import *
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def adv(request):
    return render(request,'advbook.html')


def about(request):
    appointment_count = Appointment.objects.filter(status = 'Accepted').count()
    context = {
        'appointment_count':appointment_count ,
    }

    return render(request,'about.html',context)

def user_register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        number=request.POST['number']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password'] 

        if password==confirm_password:
            Register.objects.create(
                name=name,
                email=email,
                number=number,
                password=password,
            )
        else:
            return redirect('user_register')
    return render(request,'user_register.html')

def adv_register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        number=request.POST['number']
        image=request.FILES['image']
        edu_details=request.POST['edu_details']
        edu_proof=request.FILES['edu_proof']
        achievement=request.POST['achievement']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password == confirm_password:
            Adv_Register.objects.create(
                name=name,
                email=email,
                number=number,
                image=image,
                edu_details=edu_details,
                edu_proof=edu_proof,
                achievement=achievement,
                password=password,

            )
        else:
            return redirect('adv_register')
    return render(request,'adv_register.html')

def book_adv(request):
    advocate_details = Adv_Register.objects.filter(approval = 'Approved')
    context = {
        'advocate_details':advocate_details,
    }
    return render(request,'book_adv.html', context)

def login(request):
    if request.method=='POST':
        email = request.POST['email']
        password =request.POST['password']
        if Register.objects.filter(email=email,password=password).exists():
            data= Register.objects.filter(email=email,password=password).values('name','id').first()
            request.session['u_name']=data['name']
            request.session['u_id']=data['id']
            request.session['u_email']=email
            request.session['u_password']=password

            return redirect('book_adv')
        
        elif Adv_Register.objects.filter(email=email,password=password).exists():
            data = Adv_Register.objects.filter(email=email,password=password).values('name','id').first()
            request.session['a_name']=data['name']
            request.session['a_id']=data['id']
            request.session['a_email']=email
            request.session['a_password']=password

            return redirect('adv_homepage')


        else:
            return redirect('login')

    return render(request,'login2.html')

def card_details(request,id):
    adv=Adv_Register.objects.filter(id=id)
    u_id=request.session.get('u_id')
    var=Appointment.objects.filter(user_id=u_id,advocate_id=id,status='Accepted')
    ad=Review.objects.filter(advocateid=id)
    context = {
        'adv':adv,
        'var':var,
        'ad':ad,
    }
    return render(request,'card_details.html',context)

def user_form(request, advocate_id):
    user_id = request.session.get('u_id')
    user_details = Register.objects.get(id=user_id)
    context = {
        'user_details':user_details,
        'advocate_id':advocate_id
    }
    return render(request,'user_form.html', context)


def book_appointment(request):
    user_id = request.session.get('u_id')

    if request.method == "POST":
        date = request.POST['date']
        time = request.POST['time']
        advocate_id = request.POST['advocate_id']

        Appointment.objects.create(
            user_id = Register.objects.get(id=user_id),
            date = date,
            time = time,
            advocate_id = Adv_Register.objects.get(id=advocate_id)
        )
    return render(request, "user_form.html")

def adv_homepage(request):
    adv_id = request.session.get('a_id')
    requests = Appointment.objects.filter(advocate_id = Adv_Register.objects.get(id=adv_id), status="Requested")
    context = {
        'requests':requests
    }
    return render(request,'adv_homepage.html',context)

def accept_appointment(request,appointment_id):
    Appointment.objects.filter(id=appointment_id).update(status='Accepted')
    userdetails = Appointment.objects.get(id=appointment_id).user_id
    client_email = userdetails.email
    client_name = userdetails.name

    template = render_to_string('email_template.html', {'name':client_name})
    email = EmailMessage(
        'Greetings, your appointment has been successfully booked!',
        template,
        settings.EMAIL_HOST_USER,
        [client_email],
    )
    email.fail_silently = False
    email.send()
    return redirect('adv_homepage')

def reject_appointment(request,appointment_id):
    Appointment.objects.filter(id=appointment_id).update(status='Rejected')
    return redirect('adv_homepage')

def view_advpage(request):
    adv_id = request.session.get('a_id')
    advocate_details = Adv_Register.objects.filter(approval = 'Approved').exclude(id=adv_id)
    context = {
        'advocate_details':advocate_details,
    }
    return render(request,'view_advpage.html', context)

def review(request, advocate_id):
    user_id = request.session.get('u_id')
    if request.method=='POST':
        user_review = request.POST['user_review']
        rating = request.POST['rating']

        Review.objects.create(
            user_review=user_review,
            rating=rating,
            user_id = Register.objects.get(id=user_id),
            advocateid = Adv_Register.objects.get(id=advocate_id),
        )
    
        return redirect(F'/card_details/{advocate_id}')
    # reviews=Review.objects.filter(advocateid=advocate_id)
    # print(reviews)

    context={
        'advocate_id':advocate_id
        }
    return render(request,'review.html', context)

def view_advpage2(request,id):
        adv=Adv_Register.objects.filter(id=id)
        u_id=request.session.get('u_id')
        var=Appointment.objects.filter(user_id=u_id,advocate_id=id,status='Accepted')
        ad=Review.objects.filter(advocateid=id)
        context = {
            'adv':adv,
            'var':var,
            'ad':ad,
        }
        return render(request,'view_advpage2.html')


def index(request,u_id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        message = request.POST.get('message')
       
        candidate = EmailMessage(
            name = name,
            email = email,
            message=message,
            password = password,
        )
        candidate.save()
        template = render_to_string('email_template.html', {'name':name})
        email = EmailMessage(
            'Greetings, your appointment has been successfully booked!',
            template,
            settings.EMAIL_HOST_USER,
            [email],
        )
        email.fail_silently = False
        email.send()
    return render(request,"index.html")



