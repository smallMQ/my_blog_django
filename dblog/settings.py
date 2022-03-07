
from pathlib import Path
import os
import sys

BASE_DIR = Path(__file__).resolve().parent.parent

BASE_ROOT =Path(__file__).resolve().parent

# 将根目录加入到环境变量中
sys.path.append(BASE_DIR)



SECRET_KEY = 'django-insecure-@mi_3#x=2m#zcov@7+@7*3!p7ig+jw7waum!&-7!g&g=0^uot)'



# 允许的主机
ALLOWED_HOSTS = ['*',]


INSTALLED_APPS = [
    # simpleui app注册
    # 'simpleui',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # user 表注册
    'user',
    # 跨域访问注册
    'corsheaders',
    # rf注册
    'rest_framework',
    # jwt注册,也没用到0.0
    'jwt',
    # 过滤器注册
    'django_filters',
    # md注册
    'mdeditor',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 跨域中间件注册
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'dblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


# 数据库配置
DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'new_blog',
                'USER':'smallmq',
                'PASSWORD':'wangmengqi123',
                'HOST':'127.0.0.1',
                'PORT':3306

            }
        }


# 跨域问题
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)
CORS_ALLOW_HEADERS = (
    'authorization',
    'content-type',
)




AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



# 修改时区等等
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# 关闭调试
DEBUG = False

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
#静态目录收集
# STATICFILES_DIRS = [
# os.path.join(BASE_DIR,STATIC_URL),
# ]

# 媒体文件配置
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_ROOT,'media')


# 用户自定义表注册
AUTH_USER_MODEL = 'user.UserInfo'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# rf配置
REST_FRAMEWORK = {
'PAGE_SIZE': 4,
'DEFAULT_THROTTLE_RATES':{
    'anon':'8/m',
}
}

# 缓存配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
            "DECODE_RESPONSES": True,
            "PASSWORD": "",
        }
    }
}

# 日志配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            # 实际开发建议使用WARNING
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            # 实际开发建议使用ERROR
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            # 日志位置,日志文件名,日志保存目录必须手动创建
            'filename': os.path.join(BASE_DIR, "logs", "blog.log"),
            # 日志文件的最大值,这里我们设置300M
            'maxBytes': 300 * 1024 * 1024,
            # 日志文件的数量,设置最大日志数量为10
            'backupCount': 10,
            # 日志格式:详细格式
            'formatter': 'verbose',
            # 文件内容编码
            'encoding': 'utf-8'
        },
    },
    # 日志对象
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'propagate': True, # 是否让日志信息继续冒泡给其他的日志处理系统
        },
    }
}
