from django.urls import path
from . import views

app_name = 'pi'

urlpatterns=[
    #path(' ',views.index,name = 'index'),
    #esto es por defecto pi/
    path('', views.IndexView.as_view(), name = 'index'),
    #no se si el espacio en la comilla simple puede causar algo

    #login view. Commment
	path('<slug:slug>/',views.LoginView.as_view(), name='login'),

    #ejemplo: /pi/2
    path('<int:pk>/',views.HomeView.as_view(), name='home'),

]
