from django.urls import path

from orders import views


app_name = 'orders'

urlpatterns = [
    path('', views.get_my_orders, name='my_orders'),
    path('regiter/', views.get_customer_by_email, name='get_email'),
] 