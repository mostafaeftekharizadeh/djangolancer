import random
import datetime
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from library.serializers import ModelOwnerSerializer
from .models import Room, Participate, Message
from user.user_models import Party
from user.profile_serializers import ProfileShortSerializer



class RoomSerializer(ModelOwnerSerializer):
    participates = serializers.SerializerMethodField()
    def get_participates(self, obj):
        qs = obj.chat_participate.all()
        return ParticipateSerializer(qs, context=self.context, many=True).data
    class Meta:
        model = Room
        fields = "__all__"
    def validate(self, attrs):
        project = attrs.get('project')
        party = attrs.get('party')
        user = attrs.get('user')
        if project and project.party != party and project.party != user:
            raise serializers.ValidationError("Permission Denied!")

        q1 = Q(party=user, user=party, project=project)
        q2 = Q(party=party, user=user, project=project)
        room = Room.objects.filter(q1 | q2)
        if room:
            raise serializers.ValidationError("Room Exists!")
        return attrs

    def create(self, validated_data):
        room = Room()
        room.project = validated_data.get('project')
        room.party = validated_data.get('party')
        room.user = validated_data['user']
        room.save()
        Participate.objects.create(room=room, party=room.user)
        Participate.objects.create(room=room, party=room.party)
        return room

class ParticipateSerializer(ModelOwnerSerializer):
    profile = serializers.SerializerMethodField()
    def get_profile(self, obj):
        return ProfileShortSerializer(obj.party.party_profile, context=self.context, many=False).data

    class Meta:
        model = Participate
        fields = "__all__"

class MessageSerializer(ModelOwnerSerializer):
    class Meta:
        model = Message
        fields = "__all__"
    def validate(self, attrs):
        room = attrs.get('room')
        party = attrs.get('party')
        try:
            room.chat_participate.get(party=party)
        except:
            raise serializers.ValidationError("Permission Denied!")
        return attrs
