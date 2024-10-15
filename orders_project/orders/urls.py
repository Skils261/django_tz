from django.urls import path
from .views import product_list, register, login_view, logout_view

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
