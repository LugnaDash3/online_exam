from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_detail, name='course_detail'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail_with_id'),
    path('submit/', views.submit, name='submit'),
    path('show_exam_result/', views.show_exam_result, name='show_exam_result'),
]
