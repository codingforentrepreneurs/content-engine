from django.urls import reverse 

def site_urls(request):
    project_create_url = reverse("projects:create")
    deactivate_project_url = reverse("deactivate_project")
    return {
        "home_url": reverse("home"),
        "about_url": reverse("about"),
        "project_create_url": project_create_url,
        "projects_create_url": project_create_url,
        "deactivate_project_url": deactivate_project_url,
        "deactivate_url": deactivate_project_url
    }