from rest_framework import serializers

from users.models import AdminUser


class AdminUserSerializer(serializers.ModelSerializer):
    appointment = serializers.CharField(required=False)
    role = serializers.IntegerField(required=False)
    middle_name = serializers.CharField(required=False)
    photo = serializers.FileField(required=False)

    class Meta:
        model = AdminUser
        fields = "__all__"


class TokenRefreshResponseSerializer(serializers.Serializer):
    access = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class TokenObtainPairResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()
