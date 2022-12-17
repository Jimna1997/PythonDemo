from .import views
from django.urls import path, include
app_name='movieapp'

urlpatterns = [
    path('',views.home,name='home'),
    path('movie/<int:movie_id>/',views.details,name='details'),
    path('addmovie/', views.addmovie, name='addmovie'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete')
]
