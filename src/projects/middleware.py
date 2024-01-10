from projects.models import Project

class ProjectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # print(request.session.get('project_handle'))
        project_handle= request.session.get('project_handle')
        if project_handle is not None:
            try:
                project_obj = Project.objects.get(handle=project_handle)
            except:
                project_obj = None
            request.project = project_obj
        return self.get_response(request)