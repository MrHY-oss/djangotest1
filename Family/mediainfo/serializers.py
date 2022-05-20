from rest_framework import serializers
from .models import MediaInfo

#这个是媒体网站账号密码,反序列化例子
class MediainfoSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    app_name = serializers.CharField(max_length=256)
    account = serializers.CharField(max_length=64)
    passwd = serializers.CharField(min_length=8,max_length=64)

    def validate_app_name(self,value):   #函数名必须为validate_字段名格式，否则不识别
        if value == '黄色网站':
            raise serializers.ValidationError("禁止搞黄色")
        return value

    def validate(self, attrs):
        if attrs['account'] == attrs['passwd']:
            raise serializers.ValidationError('账号密码不能一样')
        return attrs

    def create(self, validated_data):
        mediainfo = MediaInfo.objects.create(**validated_data)
        return mediainfo

    def update(self,instance,validated_data):
        instance.app_name=validated_data['app_name']
        instance.account=validated_data['account']
        instance.passwd=validated_data['passwd']
        instance.save()
        return instance



    class Meta:
        model = MediaInfo
        fields = "__all__"