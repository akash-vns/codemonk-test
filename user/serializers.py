from rest_framework import serializers
from .models import UserArticle


class AuthUserSerializerMinix:
    """get auth user from serializer context"""

    def get_auth_user(self):
        return self.context.get("request").user if "request" in self.context else None


class ArticleSerializer(serializers.ModelSerializer, AuthUserSerializerMinix):
    """article related serializer"""
    contents = serializers.ListField(child=serializers.CharField(), write_only=True)

    class Meta:
        model = UserArticle
        fields = [
            "id", "user", "content", "contents"
        ]
        extra_kwargs = {
            'user': {'required': False, "allow_null": True},
            'content': {"read_only": True}
        }

    def create(self, validated_data):
        user = self.get_auth_user()
        contents = validated_data.pop("contents", [])
        instance = None
        for content in contents:
            passing_data = {"content": content.lower(), "user": user}
            instance = super().create(passing_data)
        return instance
