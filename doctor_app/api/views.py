from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from reviews.models import Doctor, Review
from .serializers import DoctorSerializer, ReviewSerializer
from rest_framework import viewsets
from rest_framework.views import APIView


class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


@api_view(['GET', 'DELETE'])
def doctor_detail(request, pk):
    """
    GET: Подробности о враче
    DELETE: Удаление врача
    """
    doctor = get_object_or_404(Doctor, pk=pk)

    if request.method == 'GET':
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def create_review(request, doctor_pk):
    """
    POST: Создание отзыва
    """
    doctor = get_object_or_404(Doctor, pk=doctor_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(doctor=doctor)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_reviews(request, doctor_pk):
    """
    GET: Список отзывов о враче
    """
    doctor = get_object_or_404(Doctor, pk=doctor_pk)
    reviews = doctor.reviews.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_review(request, review_pk):
    """
    PUT: Обновление отзыва
    """
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewSerializer(review, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_review(request, review_pk):
    """
    DELETE: Удаление отзыва
    """
    review = get_object_or_404(Review, pk=review_pk)
    review.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

