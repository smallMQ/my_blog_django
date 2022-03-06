from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.throttling import AnonRateThrottle
from . import ser,models
from django.core.cache import cache



# 音乐api 视图接口
class music_viewset(GenericViewSet,ListModelMixin):
    serializer_class = ser.music_ser
    queryset = models.Music.objects.all()

# 关于作者api
class about_author(GenericViewSet,ListModelMixin):
    serializer_class = ser.author_about
    queryset = models.AboutAuthor.objects.all()
    # 重写list 缓存读入数据
    def list(self, request, *args, **kwargs):
        author_about = cache.get('author_about')
        if not author_about:
            queryset = self.filter_queryset(self.get_queryset())

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        return Response(author_about)


# 博客列表api
class blog_list(GenericViewSet,ListModelMixin):
    pagination_class = PageNumberPagination
    serializer_class = ser.blog_list
    filter_backends = [OrderingFilter,DjangoFilterBackend]
    filter_fields = ['view_number','tag']
    queryset = models.Blog.objects.all()

# 博客详情api
class blog_detail(GenericViewSet,ListModelMixin):
    serializer_class = ser.blog_detail
    queryset = models.Blog.objects.all()
    filter_backends = [DjangoFilterBackend,]
    filter_fields =['id']
    # 每次调用访问量+1
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).first()
        queryset.view_number += 1
        queryset.save()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

# 用户列表api
class user_list(GenericViewSet,ListModelMixin):
    serializer_class = ser.userinfo_about
    queryset = models.UserInfo.objects.all()

# 留言列表api
class message_list(GenericViewSet,ListModelMixin,CreateModelMixin):
    throttle_classes = [AnonRateThrottle]
    serializer_class = ser.message_list
    queryset = models.Message.objects.all()

# 标签列表api
class tags_list(GenericViewSet,ListModelMixin):
    serializer_class = ser.tag_list
    queryset = models.Tags.objects.all()

# 访问量api 缓存接入
class visit_view(APIView):
    def get(self,requests):
        visit_obj = models.Visit.objects.first()
        visit_obj.today_num += 1
        visit_obj.total_num +=1
        visit_obj.save()
        ser_obj = ser.visit_ser(visit_obj)
        return Response(ser_obj.data)


