from rest_framework import serializers


class ChoiceSerializer(serializers.Serializer):
    choice = serializers.CharField()


class ChoiceFieldSerializer(serializers.Serializer):
    choice_field = ChoiceSerializer(many=True)
