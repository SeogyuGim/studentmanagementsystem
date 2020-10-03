from rest_framework import serializers, viewsets
from .models import Lecture
from rest_framework.response import Response


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = (
            'id',
            'title',
            'description',
            'lecturer_name',
            'created_datetime',
            'duration',
            'slides_url',
            'is_required',
        )


class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

    def get_paginated_response(self, data):
        return Response(data)
