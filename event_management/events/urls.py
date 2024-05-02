from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events_list, name='events_list'),
    path('create/', views.create_event, name='create_event'),
    path('<int:event_id>/edit/', views.edit_event, name='edit_event'),
    path('<int:event_id>/delete/', views.delete_event, name='delete_event'),
    
    # clients
    path('clients/', views.client_list, name='client_list'),
    path('clients/create/', views.create_client, name='create_client'),
    path('clients/<int:client_id>/edit/', views.edit_client, name='edit_client'),
    path('clients/<int:client_id>/delete/', views.delete_client, name='delete_client'),
    
    # Guests
    path('guests/', views.guests_list, name='guests_list'),
    path('guests/create/', views.create_guest, name='create_guest'),
    path('guests/<int:guest_id>/edit/', views.edit_guest, name='edit_guest'),
    path('guests/<int:guest_id>/delete/', views.delete_guest, name='delete_guest'),
    
    # Employee
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/create/', views.create_employee, name='create_employee'),
    path('employees/<int:employee_id>/edit/', views.edit_employee, name='edit_employee'),
    path('employees/<int:employee_id>/delete/', views.delete_employee, name='delete_employee'),


    path('venues/', views.venue_list, name='venue_list'),
    path('venues/create/', views.create_venue, name='create_venue'),
    path('venues/<int:venue_id>/edit/', views.edit_venue, name='edit_venue'),
    path('venues/<int:venue_id>/delete/', views.delete_venue, name='delete_venue'),
    
    path('caterers/', views.caterer_list, name='caterer_list'),
    path('caterers/create/', views.create_caterer, name='create_caterer'),
    path('caterers/<int:caterer_id>/edit/', views.edit_caterer, name='edit_caterer'),
    path('caterers/<int:caterer_id>/delete/', views.delete_caterer, name='delete_caterer'),





    
]