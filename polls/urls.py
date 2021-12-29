from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    
    #polls/5/
    path('<int:quetion_id>/', views.detail, name='detail'),
    #polls/5/result
    path('<int:quetion_id>/results/', views.results, name='results'),
    #polls/5/vote
    path('<int:quetion_id>/vote/', views.vote, name='vote'),
    
]