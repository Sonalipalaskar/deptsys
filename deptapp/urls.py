from django.urls import path
from django.contrib import admin
from deptapp import views

urlpatterns = [
   path('',views.home),
   path('create',views.create),
   path('update/<int:dept_id>',views.updateDept),
   path('delete/<int:dept_id>',views.delete),  
   path('searchtext/', views.searchByText, name='search_by_text'),
   path('roles',views.role),
   path('searchtextRole/', views.searchByTextRole, name='search_by_textRole'),
   path('createrole',views.createRole),
   path('updaterole/<int:role_id>',views.updateRole),
   path('deleterole/<int:role_id>',views.deleteRole),  

    
]
