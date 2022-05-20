1\ pip install djangorestframework
    pip install markdown
    pip install django-filter
    pip install coreapi  #接口文档的模块

2\ INSTALLED_APPS   'rest_framework','应用'

REST_FRAMEWORK = {
	'DEFAULT_PERMISSION_CLASS': [
		'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
		]
}

3\ 
from django.db import models

# Create your models here.
class PhoneInfo(models.Model):
    name = models.CharField(max_length=32)
    mobilephone = models.CharField(max_length=128)
    other_contact = models.CharField(max_length=128)
    other_contact2 = models.CharField(max_length=128)
    memo = models.CharField(max_length=256)
    
4\
from rest_framework import serializers
from .models import PhoneInfo

class PhoneinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneInfo
        fields = "__all__"


5\
from .serializers import PhoneinfoSerializer
from .models import PhoneInfo

from rest_framework.viewsets import ModelViewSet

# Create your views here.
class PhoneinfoModelViewSet(ModelViewSet):
    queryset = PhoneInfo.objects.all()
    serializer_class = PhoneinfoSerializer

6\ 自己目录下新增一个urls路由
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("phoneinfo",views.PhoneinfoModelViewSet,basename="phoneinfo")

urlpattern = [

] + router.urls

7\ 创建数据库前先runserver一下加载sqlite3【懒得开mysql了 】
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser   [root/db10$ZTE]
如果要mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ssm',
        'USER': 'root',
        'PASSWORD': 'db10$ZTE',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}


8/ 自定义分页器在view定义，如果要使用全局分页器，要在setting里面设置REST_FRAMEWORK

9/ 接口文档需要引入
'DEFAULT_SCHEMA_CLASS':'rest_framework.schemas.coreapi.AutoSchema'