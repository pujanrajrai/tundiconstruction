from django.urls import path
from . import views

app_name = 'measurement_sheet'
urlpatterns = [
    path('project', views.project_list, name='project_list'),
    path('rabill/<str:project>', views.ra_bills, name='rabill'),
    path('plans/<str:project>/<str:rabill>/<str:rabill_date>', views.plans, name='plans'),
    path('activity/<str:project>/<str:rabill>/<str:rabill_date>/<str:plan>', views.activity, name='activity'),
    path('boq/<str:project>/<str:rabill>/<str:rabill_date>/<str:plan>/<str:activity>', views.boq, name='boq'),
    path('sheet/<str:project>/<str:rabill>/<str:rabill_date>/<str:plan>/<str:activity>/<str:boq>', views.sheet,
         name='sheet'),
]
