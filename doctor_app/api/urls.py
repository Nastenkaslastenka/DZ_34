
from django.urls import path
from .views import doctor_list_create, doctor_detail
from .views import DoctorListCreateAPIView
from reviews.views import create_review, list_reviews, update_review, delete_review 
from views import DoctorList, DoctorDetail

app_name = 'api'

urlpatterns = [
    path('doctors/', DoctorList.as_view()),
    path('doctors/<int:pk>/', DoctorDetail.as_view()),
    path('doctors/<int:doctor_pk>/reviews/create/', create_review, name='create-review'),
    path('doctors/<int:doctor_pk>/reviews/', list_reviews, name='list-reviews'),
    path('reviews/<int:review_pk>/update/', update_review, name='update-review'),
    path('reviews/<int:review_pk>/delete/', delete_review, name='delete-review'),
]
