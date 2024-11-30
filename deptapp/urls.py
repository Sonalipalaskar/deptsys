from django.urls import path
from django.contrib import admin
from deptapp import views

urlpatterns = [
   path('',views.home),
   path('create',views.create),
   path('update/<int:dept_id>',views.updateDept),
   path('delete/<int:dept_id>',views.delete),  
   path('searchtext/', views.searchByText, name='search_by_text'),
    
]
