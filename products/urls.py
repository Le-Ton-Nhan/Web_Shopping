from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search', views.product_search, name='product_search'),
    path('viewproduct/<str:pid>/', views.product_details, name='product_details'),
    path('cart/', views.cart_get, name='cart_get'),
]
