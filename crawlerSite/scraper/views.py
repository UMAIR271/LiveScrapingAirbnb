from django.http import HttpResponse
from django.shortcuts import render
from scraper.airbnb import Scraper
from scraper.verbo import crawler
# from scraper.test1 import Scraper
# from scraper.tests import Scraper
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .helper import *

#this is django rest api 
#this view file

class ScraperView(APIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        url = request.data.get('url')
        if "airbnb" in url:
            response = Scraper(url)
            savedataintodatabase(response)
            
            return Response({'data': response})
        elif "vrbo" in url:
            print("vrbo")
            response = crawler(url)
            return Response({'data': response})
        else:
            return Response({"sucess" : False, 'error': 'Missing URL parameter'})


    def get(self, request):
        return Response({'message': 'This endpoint requires a POST request'})


index = ScraperView.as_view()
