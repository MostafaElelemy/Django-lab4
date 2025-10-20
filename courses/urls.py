from django.urls import path
from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.course_list, name='list'),
    path('create/', views.course_create, name='create'),
    path('<str:pk>/update/', views.course_update, name='update'),
    path('<str:pk>/delete/', views.course_delete, name='delete'),
]
