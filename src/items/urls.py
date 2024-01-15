from django.urls import path, re_path

from . import views

app_name='items'
urlpatterns = [
    path("", views.item_list_view, name='list'),
    path("<int:id>/", views.item_detail_update_view, name='detail'),
    path("<int:id>/upload/", views.item_upload_view, name='upload'),
    path("<int:id>/files/", views.item_files_view, name='files'),
    re_path(r'^(?P<id>\d+)/files/(?P<name>.*)$', views.item_file_delete_view, name='files_delete'),
    path("<int:id>/edit/", views.item_detail_inline_update_view, name='edit'),
    path("<int:id>/delete/", views.item_delete_view, name='delete'),
    path("create/", views.item_create_view, name='create')
]
