from rest_framework import serializers
from .models import PhoneInfo


#这个是手机号码联系方式
class PhoneinfoSerializer(serializers.ModelSerializer):
    # sms_code = serializers.CharField(max_length=4,min_length=4)
    class Meta:
        model = PhoneInfo
        fields = "__all__"
