from django.urls import path

from customers import views


app_name = 'customers'

urlpatterns = [
    path('order_create/<str:serial>/', views.process_ordering, name='order_create'),
]
