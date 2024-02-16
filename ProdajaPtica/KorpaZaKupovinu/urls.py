from django.urls import path
from . import views

app_name = 'korpazakupovinu'
urlpatterns = [
    path('', views.DetaljiKorpe, name='DetaljiKorpe'),
    path('dodaj/<int:ptica_id>/', views.DodajUKorpu, name='DodajUKorpu'),
    path('ukloni/<int:ptica_id>/', views.UkloniIzKorpe, name='UkloniIzKorpe'),
]