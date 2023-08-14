from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet, CommentViewSet
from django.contrib import admin


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
