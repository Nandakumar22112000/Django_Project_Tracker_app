from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('new/', views.new),
    path('adminlogin/', views.adminlogin),
    path('adminpage/', views.adminpage),
    path('managerlogin/', views.managerlogin),
    path('managerpage/', views.managerpage),
    path('register/', views.registerpage),
    path('pending/', views.pending),
    path('approve/<int:id>/', views.approve),
    path('approved/', views.approved),
    path('stafflogin/', views.stafflogin),
    path('staffpage/', views.staffpage),
    path('verify/<int:id>/', views.verification),
    path('completedprojects/', views.completedprojects),
    path('verifiedprojects/', views.verified),
    path('assignproject/', views.assignProject),
    path('viewproject/', views.viewproject),
    path('unfinished/', views.unfinishedprojects),
    path('unfinishedproject/', views.unfinishedproject),
    path('newprojects/', views.newprojects),
    path('assignprojectstoteam/', views.assignprojectstoteam),
    path('employeedetails/', views.employeedetails),
    path('employeedetail/', views.employeedetail),
    path('submitproject/', views.submitproject),
    path('delete/<int:id>', views.delete),
    path('newteam/', views.newteam)
]