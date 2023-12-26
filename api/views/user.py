from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models.food import Food
from django.shortcuts import get_object_or_404
