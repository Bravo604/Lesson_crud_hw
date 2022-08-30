from django.urls import path
from . import views
urlpatterns = [
   path('course/list/', views.course_list_api, name='course_list_api'),

   path('student/list/', views.student_list_api, name='student_list_api'),


]
