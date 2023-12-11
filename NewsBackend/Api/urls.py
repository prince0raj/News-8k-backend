from django.urls import path, include
from .views import api_list, Business, Gallary, Politics, Economics, Entertainment, Lifestyle, Technoloy
from django.urls import path
from .views import api_list, business_list, gallary_list, politics_list, economics_list, entertainment_list, lifestyle_list, technoloy_list,today_post,world_news

urlpatterns = [
    path('', api_list, name="api_list"),
    path('Business/', business_list, name="business_api"),
    path('Gallary/', gallary_list, name="gallary_api"),
    path('Politics/', politics_list, name="politics_api"),
    path('Economics/', economics_list, name="economics_api"),
    path('Entertainment/', entertainment_list, name="entertainment_api"),
    path('Lifestyle/', lifestyle_list, name="lifestyle_api"),
    path('Technoloy/', technoloy_list, name="technoloy_api"),
    path('TodayPost/', today_post, name="today_post"),
    path('Worldnews/', world_news, name="world_news"),
]


