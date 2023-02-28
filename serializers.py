from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import Movie

class Movieserilizer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'description', 'image']

