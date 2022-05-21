from django.urls import path
from . import views

urlpatterns=[
   path('',views.home,name='home'),
   path('accountholder<str:pk>',views.accountholder,name='accountholder'),
   path('allaccounts',views.all_accounts,name='all_accounts'),
   path('transaction<str:pk>',views.madetransaction,name='transaction'),
   path('createuser',views.createuser,name='createuser'),
   path('updateuser<str:pk>',views.updateuser,name='updateuser'),
   path('updateaccount<str:pk>',views.updateaccount,name='updateaccount'),
   path('createaccount',views.createaccount,name='createaccount'),
   path('deleteuser<str:pk>',views.deleteuser,name='deleteuser'),
   path('deleteaccount<str:pk>',views.deleteaccount,name='deleteaccount'),
]