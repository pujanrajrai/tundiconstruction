from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    # path('sheet/', views.sheet, name='sheet'),
    path('project/', views.project_report, name='project'),
    path('project/details/<str:t_bcod>/<str:t_cact>/<str:t_cpla>/<str:t_cprj>/<str:t_rabl>', views.project_report_details, name='project_report_details'),
]
# table.t_bcod table.t_cact table.t_cpla table.t_cprj table.t_date table.t_rabl
# <str:t_bcod>/<str:t_cact>/<str:t_cpla>/<str:t_cprj>/<str:t_date>/<str:t_rabl>