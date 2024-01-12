from django.http import HttpResponse
from django_htmx.http import trigger_client_event

def render_refresh_list_view(request, response_text=""):
    custom_refresh_event = "refresh-list-view"
    response = HttpResponse(response_text)
    return trigger_client_event(response,custom_refresh_event)