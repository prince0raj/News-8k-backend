from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from NewsApp.serializers import BusinessSerializer, GallarySerializer, PoliticsSerializer, EconomicsSerializer, EntertainmentSerializer, LifestyleSerializer, TechnoloySerializer,TodayPostSerializer, WorldnewsSerializer
from NewsApp.models import Business, Gallary, Politics, Economics, Entertainment, Lifestyle, Technoloy,TodayPost,Worldnews


@api_view(['GET'])
def api_list(request):
    api_list_data = {
        'Business': "Get All news related to Business",
        'Gallary': "Get All news related to Gallary",
        'Politics': "Get All news related to Politics",
        'Economics': "Get All news related to Economics",
        'Entertainment': "Get All news related to Entertainment",
        'Lifestyle': "Get All news related to Lifestyle",
        'Technoloy': "Get All news related to Technoloy",
        'TodayPost': "Get All news related to TodayPost",
        'Worldnews': "Get All news related to Worldnews",
    }
    return Response(api_list_data)


@api_view(['GET'])
def business_list(request):
    queryset = Business.objects.all()
    data = BusinessSerializer(queryset, many=True).data
    for item in data:
        item['category'] = 'Business'
    return Response(data)

@api_view(['GET'])
def gallary_list(request):
    queryset = Gallary.objects.all()
    data = GallarySerializer(queryset, many=True).data
    return Response(data)

@api_view(['GET'])
def politics_list(request):
    queryset = Politics.objects.all()
    data = PoliticsSerializer(queryset, many=True).data
    for item in data:
        item['category'] = 'Politics'
    return Response(data)

@api_view(['GET'])
def economics_list(request):
    queryset = Economics.objects.all()
    data = EconomicsSerializer(queryset, many=True).data
    for item in data:
        item['category'] = 'Economics'
    return Response(data)

@api_view(['GET'])
def entertainment_list(request):
    queryset = Entertainment.objects.all()
    data = EntertainmentSerializer(queryset, many=True).data
    for item in data:
        item['category'] = 'Entertainment'
    return Response(data)

@api_view(['GET'])
def lifestyle_list(request):
    queryset = Lifestyle.objects.all()
    data = LifestyleSerializer(queryset, many=True).data
    for item in data:
        item['category'] = 'Lifestyle'
    return Response(data)

@api_view(['GET'])
def technoloy_list(request):
    queryset = Technoloy.objects.all()
    data = TechnoloySerializer(queryset, many=True).data
    for item in data:
        item['category'] = 'Technoloy'
    return Response(data)

@api_view(['GET'])
def today_post(request):
    queryset =TodayPost.objects.all()
    data = TodayPostSerializer(queryset, many=True).data
    for item in data:
        item['category'] = 'TodayPost'
    return Response(data)    

@api_view(['GET'])
def world_news(request):
    queryset =Worldnews.objects.all()
    data = WorldnewsSerializer(queryset, many=True).data
    for item in data:
        item['category'] = 'Worldnews'
    return Response(data)    
