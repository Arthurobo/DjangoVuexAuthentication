from jobs.models import BusinessPageJobs, IndividualJobs
from .serializers import BusinessPageJobsSerializer, IndividualPageJobsSerializer
from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser, JSONParser
from django.http import request
from rest_framework.response import Response
from rest_framework.views import APIView

class BusinessPageJobsListApiView(generics.ListCreateAPIView):
    queryset = BusinessPageJobs.objects.all()
    serializer_class = BusinessPageJobsSerializer


class BusinessPageJobsDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BusinessPageJobs.objects.all()
    serializer_class = BusinessPageJobsSerializer


class IndividualJobsListApiView(APIView):
    queryset = IndividualJobs.objects.all().order_by('-date_created')
    serializer_class = IndividualPageJobsSerializer
    parser_classes = [MultiPartParser,FormParser,JSONParser]


    def get(self, request, format=None):
        tests = IndividualJobs.objects.all()
        serializer = IndividualPageJobsSerializer(tests, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def post(self, request, format=None):
        print(request.data)
        serializer = IndividualPageJobsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IndividualJobsDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IndividualJobs.objects.all()
    serializer_class = IndividualPageJobsSerializer
