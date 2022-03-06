
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.static import serve
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('user.urls')),
    # md 路由配置接口
    re_path('mdeditor/', include('mdeditor.urls')),
    # 暴露文件接口
    re_path(r'^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),

]
