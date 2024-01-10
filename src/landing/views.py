from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    print(request.session.get('project_handle'))
    return render(request, "landing/home.html", {})

def server_error_page(request):
    raise Exception
    return render(request, "landing/error.html", {})