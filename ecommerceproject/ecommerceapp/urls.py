
from django.contrib import admin
from . import views
from django.urls import path,include
app_name='ecommerceapp'

urlpatterns = [
    path('',views.allProductCategory,name='allProductCategory'),
    path('<slug:c_slug>/',views.allProductCategory,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.productDetail,name='productDetail'),
]
