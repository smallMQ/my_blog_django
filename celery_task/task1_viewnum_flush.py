# coding:utf-8


from .celery import app
from django.core.cache import cache
from user import models,ser

# 每日访问量任务更新
@app.task
def view_num_update():
    number = models.Visit.objects.first()
    number.today_num = 0
    number.save()
    return True

# 作者信息缓存任务
@app.task
def about_author_update():
    author = models.AboutAuthor.objects.all()
    ser_author = ser.author_about(instance=author,many=True)
    for i in ser_author.data:
        i['avator'] ='http:127.0.0.1:8000'+i['avator']
    cache.set('author_about',ser_author.data,60*60)
    print(ser_author)
    return True

# celery --app=celery_task worker -l info -P eventlet --pool=solo
# celery -A celery_task beat -l info
