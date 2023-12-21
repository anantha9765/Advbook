from django.urls import path
from advbook_app import views

urlpatterns = [
    path('',views.adv,name='adv'),
    path('about',views.about,name="about"),
    path('user_register',views.user_register,name="user_register"),
    path('adv_register',views.adv_register,name="adv_register"),
    path('login',views.login,name="login"),
    path('book_adv',views.book_adv,name="book_adv"),
    path('card_details/<int:id>',views.card_details,name="card_details"),
    path('adv_homepage',views.adv_homepage,name="adv_homepage"),
    path('user_form/<int:advocate_id>',views.user_form,name="user_form"),
    path('book_appointment',views.book_appointment,name="book_appointment"),
    path('accept_appointment/<int:appointment_id>',views.accept_appointment,name="accept_appointment"),
    path('reject_appointment/<int:appointment_id>',views.reject_appointment,name="reject_appointment"),
    path('view_advpage',views.view_advpage,name="view_advpage"),
    path('review/<int:advocate_id>',views.review,name="review"),
    path('view_advpage2<int:id>',views.view_advpage2,name="view_advpage2"),


    
    ]
