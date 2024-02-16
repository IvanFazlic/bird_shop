from django.urls import path
from . import views
app_name = 'salonptica'
urlpatterns = [ 
    path('', views.ListaPtica, name='ListaPtica'),
    path('<slug:segment_slug>/', views.ListaPtica, name='ListaPticaPoSegmentu'),
    path('<int:id>/<slug:slug>/', views.DetaljiPtica, name='DetaljiPtica'), 
]