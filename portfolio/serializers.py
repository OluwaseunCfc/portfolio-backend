from rest_framework import serializers
from .models import Project, Experience, GalleryImage


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'description',
            'image',
            'live_demo_url',
            'github_url',
            'category',
            'status',
            'tech_stack',
            'is_featured',
            'date_added',
        ]


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            'id',
            'company',
            'role',
            'start_date',
            'end_date',
            'is_current',
            'description',
        ]


class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = [
            'id',
            'image',
            'caption',
            'date_added',
        ]