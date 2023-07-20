from django.urls import path, include
from . import views



app_name = 'tasks'


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('update/<int:pk>/', views.TaskUpdateView.as_view(), name = 'update'),
    path('detail/<int:pk>/', views.TaskDetailView.as_view(), name = 'detail'),
    path('delete/<int:pk>/', views.DeleteTaskView.as_view(), name='delete'),
]
