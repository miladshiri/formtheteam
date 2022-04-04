from django.urls import path 
from team.views import teams_list


urlpatterns = [
    path('list', teams_list, name='list')
]