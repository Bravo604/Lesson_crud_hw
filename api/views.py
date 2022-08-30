import json
from django.shortcuts import render
from codify.models import Course, Student
from django.core import serializers
from django.http import JsonResponse


def course_list_api(request):
    courses = Course.objects.all()

    serialized_courses = serializers.serialize('json', list(courses))
    return JsonResponse(serialized_courses, safe=False)


def student_list_api(request):
    students = Student.objects.all()

    serialized_students = serializers.serialize('json', list(students))
    return JsonResponse(serialized_students, safe=False)
