from django.urls import path
from . import views

app_name = 'project'
urlpatterns = [
    path('tender/reports/', views.tender_reports, name='tender_reports'),
    path('tender/reports/details/<str:str>', views.tender_details_reports, name='tender_reports_details'),

]
