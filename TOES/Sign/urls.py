from django.urls import path
from . import views

urlpatterns = [

    path('' , views.getin ),
    path('sign_in/', views.sign_in ,name ='sign_in'),
    path('sign_up/' , views.sign_up , name = 'sign_up'),
    path('forget_pass', views.forget_pass , name = 'forget_pass'),
]
