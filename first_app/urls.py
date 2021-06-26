from django.urls import path
from . import views



urlpatterns = [
    path('', views.root),
    path('first_app/blogs', views.index),
    path('first_app/blogs/new', views.new),
    path('first_app/blogs/create', views.create),
    path('first_app/blogs/<int:num>', views.show),
    path('first_app/blogs/<int:num>/edit', views.edit),
    path('first_app/blogs/<int:num>/delete', views.destroy),
    path('first_app/blogs/bonus', views.bonus),
   
]
