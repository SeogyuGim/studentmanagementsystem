from rest_framework import serializers, viewsets
from .models import Certificate
from rest_framework.response import Response


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = (
            'id',
            'name',
            'description',
            'created_datetime',
            'updated_datetime',
        )


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

    def get_paginated_response(self, data):
        return Response(data)
