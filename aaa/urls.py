from django.urls import path

from . import views

app_name = 'aaa'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('detail/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('results/<int:course_point>/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('vote/', views.vote, name='vote'),
]