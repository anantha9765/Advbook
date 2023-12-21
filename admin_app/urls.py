from django.urls import path
from admin_app import views

urlpatterns = [
    path('data',views.data,name="data"),
    path('admin1',views.admin1,name="admin1"),
    path('view_user_details',views.view_user_details,name="view_user_details"),
    path('view_adv_details',views.view_adv_details,name="view_adv_details"),
    path('approve_admin/<int:advocate_id>',views.approve_admin,name="approve_admin"),
    path('reject_admin/<int:advocate_id>',views.reject_admin,name="reject_admin"),
    path('view_approved_adv',views.view_approved_adv,name="view_approved_adv"),
    path('view_rejected_adv',views.view_rejected_adv,name="view_rejected_adv"),
]