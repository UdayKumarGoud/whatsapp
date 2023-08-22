from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from ..models import AppUser

class AuthTokenSerializer(serializers.Serializer):
    mobile = serializers.CharField()

    def validate(self, attrs):
        mobile = attrs.get('mobile')

        if AppUser.objects.filter(mobile=mobile).exists():
            user = AppUser.objects.get(mobile=mobile)
        else:
            msg = _('mobile is not Created')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs