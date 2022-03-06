from django.db import models
from mdeditor.fields import MDTextField

from django.contrib.auth.models import AbstractUser

# 用户表
class UserInfo(AbstractUser):
    telephone = models.CharField(max_length=11,verbose_name='电话',default='16639821093',unique=True)
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = '用户表'

# 分类表
class Tags(models.Model):
    name = models.CharField(max_length=32,verbose_name='分类表',null=True)
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'

    def __str__(self):
        return self.name

# 博客表
class Blog(models.Model):
    theme = models.CharField(max_length=64,verbose_name='题目',null=True)
    simple_introduction = models.CharField(max_length=128,verbose_name='简介',null=True)
    content = MDTextField(verbose_name='内容',null=True)
    create_time = models.DateField(auto_now_add=True,verbose_name='创建时间')
    view_number = models.IntegerField(verbose_name='访问量',default=0)
    photo = models.ImageField(upload_to='blog_photo',verbose_name='图片',null=True)
    author = models.ForeignKey(to=UserInfo,verbose_name='作者名字',on_delete=models.DO_NOTHING)
    tag = models.ManyToManyField(to=Tags,verbose_name='分类')

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = '博客'


# 留言表
class Message(models.Model):
    create_time = models.DateField(auto_now_add=True,verbose_name='留言时间')
    content = models.CharField(max_length=256,verbose_name='留言内容')
    user = models.CharField(max_length=32,verbose_name='留言人名字')

    def __str__(self):
        return self.content[:10]
    class Meta:
        verbose_name = '留言'
        verbose_name_plural = '留言'


# 访问表
class Visit(models.Model):
    create_time = models.DateField(auto_now_add=True,verbose_name='访问时间')
    today_num = models.IntegerField(verbose_name='今日访问量',default=0)
    total_num = models.IntegerField(verbose_name='今日访问量',default=0)

    class Meta:
        verbose_name = '访问信息'
        verbose_name_plural = '访问信息'

# 音乐表
class Music(models.Model):
    title = models.CharField(max_length=32,verbose_name='歌曲名字')
    artist = models.CharField(max_length=32,verbose_name='歌手')
    url = models.URLField(verbose_name='歌曲链接',max_length=400)
    cover = models.URLField(verbose_name='图片链接',null=True,max_length=400)
    lrc = models.TextField(verbose_name='歌词',null=True)
    class Meta:
        verbose_name = '音乐'
        verbose_name_plural = '音乐'
    def __str__(self):
        return self.title




class AboutAuthor(models.Model):
    name = models.CharField(max_length=32,verbose_name='昵称',default='smallMQ')
    personal_signature = models.CharField(max_length=128,verbose_name='个性签名',default='爱屋及乌')
    email = models.CharField(max_length=32,verbose_name='邮箱',default='2271443486@qq.com')
    we_chat = models.CharField(max_length=32,verbose_name='微信',default='16639821093')
    telephone = models.CharField(max_length=11,verbose_name='电话',default='16639821093')
    age = models.CharField(max_length=8,verbose_name='年龄',default='21')
    expect_job = models.CharField(max_length=32,verbose_name='求职岗位',null=True)
    expect_salary = models.CharField(max_length=8,verbose_name='期望薪水',null=True)
    graduation_school = models.CharField(max_length=32,verbose_name='毕业院校',default='河南农业大学')
    graduation_time = models.CharField(max_length=128,verbose_name='毕业时间',default='2023')
    certificate = models.CharField(max_length=128,verbose_name='证书',null=True)
    simple_experience = models.TextField(verbose_name='工作经验简历',null=True)
    avator = models.ImageField(upload_to='avator',verbose_name='头像',null=True)


    def __str__(self):
        return '关于作者'
    class Meta:
        verbose_name = '关于作者'
        verbose_name_plural = '关于作者'


class JobExperience(models.Model):
    company_name = models.CharField(max_length=32, verbose_name='公司名称',null=True)
    job_name = models.CharField(max_length=32, verbose_name='职位名称',null=True)
    job_time = models.CharField(max_length=32, verbose_name='在职时间',null=True)
    salary = models.CharField(max_length=32, verbose_name='薪水',null=True)
    job_content = models.TextField(verbose_name='工作内容',null=True)
    job_author = models.ForeignKey(to=AboutAuthor,verbose_name='作者',on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = '工作经历'
        verbose_name_plural = '工作经历'
