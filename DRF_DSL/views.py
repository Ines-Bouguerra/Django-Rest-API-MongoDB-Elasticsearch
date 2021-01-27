from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
   
from DRF_DSL.models import University
from DRF_DSL.serializers import DRF_DSLSerializer
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def university_list(request):
    if request.method == 'GET':
        universities = University.objects.all()
        name = request.GET.get('name', None)
        if name is not None:
            universities = universities.filter(title__icontains=name)
        DRF_DSL_Serializer = DRF_DSLSerializer(universities, many=True)
        return JsonResponse(DRF_DSL_Serializer.data, safe=False)
   