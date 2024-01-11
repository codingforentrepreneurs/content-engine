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
from django.urls import path, include

from landing import views as landing_views
from projects import views as projects_views

urlpatterns = [
    path("",    landing_views.home_page_view, name='home'),
    path("items/", include('items.urls')),
    path("projects/", include('projects.urls')),
    path("about/",    landing_views.about_page_view, name='about'),
    path("activate/project/<slug:handle>/", 
          projects_views.activate_project_view, name='activate_project'),
    path("deactivate/project/", 
           projects_views.deactivate_project_view, name='deactivate_project'),
    path("admin/", admin.site.urls),
]
