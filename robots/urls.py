from django.urls import path

from robots import views


app_name = 'robots'

urlpatterns = [
    path('add/', views.CreateRobotView.as_view(), name='add_robot'),
    path('get_excel/', views.get_excel_file, name='get_excel'),
    path('catalog/', views.get_all_robots, name='get_all_robots'),
]