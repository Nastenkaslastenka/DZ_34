
from django.db.models import Count, Avg
from rest_framework import serializers 
from reviews.models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    review_count = serializers.IntegerField(source='reviews.count', read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'specialty', 'created_at', 'review_count', 'average_rating']

    def get_average_rating(self, obj):
        agg = obj.reviews.aggregate(avg=Avg('rating'))
        return agg['avg'] or 0
from reviews.models import Review
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'