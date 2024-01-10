"""
URL configuration for cfehome project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from landing import views as landing_views
from projects import views as projects_views

urlpatterns = [
    path("",    landing_views.home_page_view),
    path("activate/project/<slug:handle>/", 
          projects_views.activate_project_view),
     path("deactivate/project/<slug:handle>/", 
           projects_views.deactivate_project_view),
    path("err",    landing_views.server_error_page),
    path("admin/", admin.site.urls),
]
