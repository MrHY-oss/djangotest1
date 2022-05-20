import json

from django.views import View
from .serializers import MediainfoSerializer
from django.http.response import JsonResponse
from .models import MediaInfo

class MediainfoView(View):
    def get(self,request):
        mediainfo = MediaInfo.objects.all()
        #实例序列化器，得到序列化对象
        serializer = MediainfoSerializer(mediainfo,many=True)
        #调用序列化对象的data属性方法获取转换后的数据
        data = serializer.data
        return JsonResponse(data=data,status=200,safe=False)

    def post(self,request):
        #获取前端数据
        data = request.body.decode()
        data_dict = json.loads(data)
        #验证数据
        serializer = MediainfoSerializer(data=data_dict)
        serializer.is_valid()   #验证方法
        #保存数据
        serializer.save()
        #返回结果
        return JsonResponse(serializer.data)

    def put(self,request,pk):
        data = request.body.decode()
        data_dict = json.loads(data)

        try:
            info = MediaInfo.objects.get(id=pk)
        except:
            return JsonResponse("error",status=400)

        serilizer = MediainfoSerializer(info,data=data_dict)
        serilizer.is_valid()
        serilizer.save()

        return JsonResponse(serilizer.data)


class MediainfoOneView(View):
    def get(self,request):
        mediainfo = MediaInfo.objects.get(app_name="腾讯视频")   #不知道为啥用get不起，filter倒是能过
        #实例序列化器，得到序列化对象
        serializer = MediainfoSerializer(mediainfo)
        #调用序列化对象的data属性方法获取转换后的数据
        data = serializer.data
        return JsonResponse(data=data)
