from rest_framework import serializers

class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(min_length=1,max_length=255)
    description=serializers.CharField(max_length=100000, min_length=0, allow_blank=True,allow_null=True, default=None, required=False)
    completed = serializers.BooleanField(default=False)
    