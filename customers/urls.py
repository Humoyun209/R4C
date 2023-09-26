from django.urls import path

from customers import views


app_name = 'customers'

urlpatterns = [
    path('order_create/<str:model>/<str:version>/', views.get_email_from_customer, name='order_create'),
]
