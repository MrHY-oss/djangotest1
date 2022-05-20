from rest_framework.decorators import action

from .serializers import PhoneinfoSerializer
from .models import PhoneInfo
from rest_framework.viewsets import ModelViewSet

#导入排序类
from rest_framework.filters import OrderingFilter
#导入分页器类
from rest_framework.pagination import PageNumberPagination


#
from django.views import View
from django.http.response import JsonResponse

# Create your views here.

#自定义分页器
class PageNum(PageNumberPagination):
    page_size_query_param = 'page_size' #指定控制每页数量的参数
    max_page_size = 1 #指定每页最大返回数


class PhoneinfoModelViewSet(ModelViewSet):
    queryset = PhoneInfo.objects.all()
    serializer_class = PhoneinfoSerializer
    #setting里面导入过滤的框架，就可以进行过滤
    filter_fields = ('id','name','mobilephone')
    #http://127.0.0.1:8000/api/phoneinfo/?id=2
    #排序操作，导入排序，指定排序字段
    filter_backends = [OrderingFilter]
    ordering_fields = ('id','name','mobilephone')
    #http://127.0.0.1:8000/api/phoneinfo/?ordering=mobilephone

    #分页操作
    pagination_class = PageNum
    #http://127.0.0.1:8000/api/phoneinfo/?page=1&page_size=2
    #page表示展示第几页，page_size表示每页最大展示多少条

    @action(methods=['get'],detail=False)
    def lastdata(self,request,pk):
        phoneinfo = PhoneInfo.objects.get(mobilephone=pk)
        serializer = PhoneinfoSerializer(phoneinfo)
        return JsonResponse(serializer.data)



