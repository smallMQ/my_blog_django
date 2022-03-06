from django.urls import path,include,re_path
from . import views
# 自动生成路由
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
# 注册路由
router.register('music',views.music_viewset,'music')
router.register('author',views.about_author,'author')
router.register('blog',views.blog_list,'blog')
router.register('user',views.user_list,'user')
router.register('message',views.message_list,'message')
router.register('tags',views.tags_list,'tags')
router.register('detail',views.blog_detail,'detail')

urlpatterns = [
    # 导入路由
    path('', include(router.urls)),
    path('viewnum/',views.visit_view.as_view())
]
