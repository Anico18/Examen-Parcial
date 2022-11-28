from . import views
from django.urls import path 

app_name = 'gestion_tareas'

urlpatterns = [
    path('',views.index, name='index'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('new',views.new,name='new'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('info/<int:id>', views.info, name='info')
]