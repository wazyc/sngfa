from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.map, name='map'),
    path('alldata/', views.alldata, name='alldata'),
    path('detail/<str:machine>', views.detail, name='detail'),
]
