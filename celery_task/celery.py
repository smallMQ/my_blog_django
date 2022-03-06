'''
作者:smallMQ

'''

from celery import Celery

# 配置broker 和 backend
broker = 'redis://127.0.0.1:6379/1'
backend = 'redis://127.0.0.1:6379/2'

# 加载django 环境
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dblog.settings')

# 注册
app = Celery(__name__,broker=broker,backend=backend,include=('celery_task.task1_viewnum_flush'))
# 时区配置
app.conf.timezone = 'Asia/shanghai'
app.conf.enable_utc = False
# debug false
worker_hijack_root_logger = False


from datetime import timedelta
from celery.schedules import crontab

# 任务配置
app.conf.beat_schedule = {
    'update_task':{
        'task': 'celery_task.task1_viewnum_flush.about_author_update',
        'schedule': timedelta(seconds=60*60),
    },
    'up_task': {
        'task': 'celery_task.task1_viewnum_flush.view_num_update',
        'schedule': crontab(minute=1,hour=1)
        # 'args': (16, 16),
    },
}


