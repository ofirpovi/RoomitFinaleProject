from django.urls import path

from . import views as app_views

urlpatterns = [
    path('', app_views.post_list, name='post_list_page'),
    path('requirementsR/<str:username>/', app_views.requirementsR, name='requirementsR'),
    path('requirementsP/<str:username>/', app_views.requirementsP, name='requirementsP'),
    path('more/', app_views.more, name='more'),
    # path('search-results', app_views.search, name='search-results')
    path('like-picture/', app_views.like_picture, name='like_picture'),
]

