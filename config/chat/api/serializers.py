from rest_framework import serializers

from ..models import Room


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    participants = serializers.StringRelatedField(many=True)

    class Meta:
        model = Room
        fields = ['id', 'author', 'title', 'messages', 'participants']
