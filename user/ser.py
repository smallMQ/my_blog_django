from rest_framework.serializers import ModelSerializer,PrimaryKeyRelatedField

from . import models

# 音乐序列化
class music_ser(ModelSerializer):
    class Meta:
        model = models.Music
        fields = ['title','artist','url','cover','lrc']

# 关于作者序列化
class author_about(ModelSerializer):
    class Meta:
        model = models.AboutAuthor
        fields = '__all__'

# 用户序列化
class userinfo_about(ModelSerializer):
    class Meta:
        model = models.UserInfo
        fields = ('username',)

# 博客列表序列化
class blog_list(ModelSerializer):
    author = userinfo_about()
    class Meta:
        model = models.Blog
        fields = ['id','theme','simple_introduction','create_time','view_number','photo','author','tag']

# 博客详情序列化
class blog_detail(ModelSerializer):
    author = userinfo_about()
    class Meta:
        model = models.Blog
        fields = ['id','content','author','create_time','view_number']


# 留言序列化
class message_list(ModelSerializer):
    class Meta:
        model = models.Message
        fields = '__all__'

# 标签序列化
class tag_list(ModelSerializer):
    class Meta:
        model = models.Tags
        fields = '__all__'


class visit_ser(ModelSerializer):
    class Meta:
        model = models.Visit
        fields = ['today_num','total_num']