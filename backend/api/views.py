from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import hashlib


def home(request):
    return JsonResponse({"message": "hello! (message from Django)"})

