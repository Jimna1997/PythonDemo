from django.contrib import admin
from django.urls import path
from .import views

app_name='todoapp'
urlpatterns = [
    path('', views.add,name='add'),
    path('cbvhome/',views.TaskListView.as_view(),name='cbvhome'),
    path('cbvdetails/<int:pk>/', views.TaskDetailView.as_view(), name='cbvdetails'),
    # path('details',views.details,name='details'),
    path('/delete<int:taskid>/', views.delete, name='delete'),
    path('/update<int:taskid>/', views.update, name='update'),
    path('cbvupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cbvdelete'),

]
