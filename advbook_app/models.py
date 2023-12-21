from django.db import models

class Register(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    number =models.CharField(max_length=10)
    password=models.CharField(max_length=30)
    registered_at = models.DateTimeField(auto_now_add=True)

class Adv_Register(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    number=models.CharField(max_length=10)
    image=models.ImageField(upload_to='imgfile',default='null.jpg')
    edu_details=models.CharField(max_length=50)
    edu_proof=models.ImageField(upload_to='imgfile',default='null.jpg')
    achievement=models.TextField(default='No achievement')
    password=models.CharField(max_length=30)
    registered_at = models.DateTimeField(auto_now_add=True)
    approval = models.CharField(max_length=50,default='waiting for approval')

class Appointment(models.Model):
    user_id = models.ForeignKey(Register, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    advocate_id = models.ForeignKey(Adv_Register, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='Requested')
    booked_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    user_id=models.ForeignKey(Register, on_delete=models.CASCADE)
    advocateid=models.ForeignKey(Adv_Register, on_delete=models.CASCADE)
    user_review=models.TextField()
    rating=models.FloatField()
    date=models.DateField(auto_now=True)