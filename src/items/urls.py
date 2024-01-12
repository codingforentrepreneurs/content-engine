from django.urls import path

from . import views

app_name='items'
urlpatterns = [
    path("", views.item_list_view, name='list'),
    path("<int:id>/", views.item_detail_update_view, name='detail'),
    path("<int:id>/edit/", views.item_detail_inline_update_view, name='edit'),
    path("<int:id>/delete/", views.item_delete_view, name='delete'),
    path("create/", views.item_create_view, name='create')
]
