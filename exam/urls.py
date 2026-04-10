from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_detail, name='course_detail'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail_with_id'),
    path('lessons/<int:lesson_id>/submit/', views.submit, name='submit'),
    path('submissions/<int:submission_id>/result/', views.show_exam_result, name='show_exam_result'),
]
