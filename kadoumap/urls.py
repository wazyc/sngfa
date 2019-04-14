from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.all, name='all'),
    path('detail/<str:machine>', views.detail, name='detail'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
