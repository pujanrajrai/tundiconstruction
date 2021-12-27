from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('project/', include('project.urls')),
    path('measurement/', include('measurementsheet.urls')),
    path('reports/', include('reports.urls')),
]

