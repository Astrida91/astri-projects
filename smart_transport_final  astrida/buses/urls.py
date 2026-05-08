from django.urls import path
from . import views


app_name = 'buses'

urlpatterns = [
    path('', views.bus_list, name='bus_list'),  # List all buses
    path('<int:pk>/', views.bus_details, name='bus_details'),  # View bus details
    path('<int:pk>/book/', views.book_ticket, name='book_ticket'),  # Book a ticket
    path('<int:pk>/buses/', views.ticket_confirmation, name='ticket_confirmation'),  # Book a ticket


    
]
