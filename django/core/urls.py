from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.about, name='about'),
    path('serviços/', views.services, name='services'),
    path('contato/', views.contact, name='contact'),
    path('produto/avaliar/', views.product_evaluation, name='product_evaluation'),
    path('contato/mensagem/enviar/', views.send_message, name='send_message')
]