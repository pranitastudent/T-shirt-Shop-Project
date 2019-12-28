from django.urls import path
from .views import all_products
from django.conf.urls import url
from .views import (get_feedback, add_feedback, edit_feedback, delete_feedback, detail_feedback)

urlpatterns = [
    path('get_feedback/', get_feedback, name='get_feedback'), 
    path('<int:pk>/add_feedback', add_feedback, name= 'add_feedback'),
    path('<int:pk>/edit_feedback', edit_feedback, name='edit_feedback'),
    path('<int:pk>/delete_feedback', delete_feedback, name='delete_feedback'),
    path('<int:pk>/detail_feedback', detail_feedback, name='detail_feedback'),
        
   
      
]