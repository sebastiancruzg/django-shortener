from rest_framework import serializers


class UrlSerializer(serializers.Serializer):
    originalUrl = serializers.URLField
    shortUrl = serializers.URLField
    createdAt = serializers.DateTimeField
