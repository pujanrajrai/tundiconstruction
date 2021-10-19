from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    # path('sheet/', views.sheet, name='sheet'),
    path('project/', views.project_report, name='project'),
    path('project/details/<str:str>', views.project_report_details, name='project_report_details'),
]
